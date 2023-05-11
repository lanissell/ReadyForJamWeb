from django.forms import model_to_dict
from django.http import JsonResponse

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View

from jam.forms import JamRegistrationForm, JamColorForm, JamDateForm, JamCriteriaFormSet
from jam.models import Jam, JamColor, JamDate, JamCriteria, Participant
from jam.utils import JamCard, JamFormSaver, GetJamFormContext, LocalizeDate, GetCurrentDate, \
    IsParticipant, IsAuthor


class JamRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        if request.user.is_authenticated:
            context = GetJamFormContext()
            return render(request, '/jam/jam-registration.html', context=context)
        else:
            return redirect('login')

    @staticmethod
    def post(request, **kwargs):
        form = JamRegistrationForm(request.POST, request.FILES)
        color = JamColorForm(request.POST)
        date = JamDateForm(request.POST)
        criteria = JamCriteriaFormSet(request.POST)

        formSaver = JamFormSaver()
        formSaver.MainFormSave(form, request)
        formSaver.RelativeFormsSave([color])
        formSaver.DateFormSave(date)
        formSaver.FormsetSaver(criteria)
        if formSaver.isFormsValidated:
            formSaver.SaveRelativeObjects()
            return redirect(f'../../jam/{formSaver.mainObject.name}/')
        else:
            context = GetJamFormContext(form, color, date, criteria)
            return render(request, '/jam/jam-registration.html', context=context)
        

class JamUpdateView(View):
    baseContext = {
        'title': 'Обновление джема',
        'btnName': 'Обновить'
    }

    def get(self, request, **kwargs):
        user = request.user
        if user.is_authenticated:
            jamObject = Jam.objects.get(name__exact=kwargs['jamName'])
            if jamObject.author.id == user.id:
                context = self.GetJamInstanceContext(jamObject)
                context.update(self.baseContext)
                return render(request, '/jam/jam-registration.html/', context=context)
            else:
                return redirect('jamList')
        else:
            return redirect('login')

    @staticmethod
    def GetJamInstanceContext(jamObject):
        colorObject = JamColor.objects.get(jam=jamObject)
        dateObject = JamDate.objects.get(jam=jamObject)
        criteriaObject = JamCriteria.objects.filter(jam=jamObject)

        jam = JamRegistrationForm(instance=jamObject)
        color = JamColorForm(instance=colorObject)
        date = JamDateForm(instance=dateObject)
        criteria = JamCriteriaFormSet(queryset=criteriaObject)
        return GetJamFormContext(jam, color, date, criteria)

    def post(self, request, **kwargs):
        jamObject = Jam.objects.get(name__exact=kwargs['jamName'])
        jam = JamRegistrationForm(request.POST, request.FILES,
                                  instance=jamObject)
        color = JamColorForm(request.POST)
        date = JamDateForm(request.POST)

        criteriaObjects = JamCriteria.objects.filter(jam=jamObject)
        criteria = JamCriteriaFormSet(request.POST, queryset=criteriaObjects)

        if jam.is_valid() and color.is_valid() \
                and date.is_valid() and criteria.is_valid():
            Jam.objects.update_or_create(id=jamObject.id,
                                         defaults=jam.cleaned_data)
            JamColor.objects.update_or_create(jam=jamObject,
                                              defaults=color.cleaned_data)
            JamDate.objects.update_or_create(jam=jamObject,
                                             defaults=date.cleaned_data)

            self.DeleteRedundantCriteria(criteria.cleaned_data, criteriaObjects)
            formSaver = JamFormSaver()
            formSaver.FormsetSaver(criteria, jamObject)
            formSaver.SaveRelativeObjects()

            return redirect(f'/jam/{jamObject.name}/')
        else:
            context = GetJamFormContext(jam, color, date)
            context.update(self.baseContext)
            return render(request, '/jam/jam-registration.html', context=context)

    @staticmethod
    def DeleteRedundantCriteria(template, allObjects):
        criteriaToSave = [c['id'] for c in template
                          if c.get('name', '') != '']
        criteriaToDelete = [c for c in allObjects
                            if c not in criteriaToSave]
        for c in criteriaToDelete:
            c.delete()


class JamPageView(View):

    @staticmethod
    def get(request, jamName, **kwargs):
        jam = None
        context = {}
        try:
            jam = Jam.objects.get(name=jamName)
        except ObjectDoesNotExist:
            print('jam not found')
        if jam is not None:
            jamColor = JamColor.objects.get(jam=jam)
            context['jam'] = jam
            context['jamColor'] = jamColor
            return render(request, '/jam/jam-page.html', context=context)
        else:
            return redirect('jamList')

class JamDeleteView(View):

    @staticmethod
    def get(request, **kwargs):
        user = request.user
        if user.is_authenticated:
            jamObject = Jam.objects.get(name__exact=kwargs['jamName'])
            if IsAuthor(user, jamObject):
                jamObject.delete()
            return redirect('jamList')
        else:
            return redirect('login')


class JamListView(View):

    _query = '''
            SELECT  jam_jam.id, 
                    jam_jam.name, 
                    jam_jam.avatar,
                    jam_jamcolor.background_color,
                    jam_jamdate.start_date,
                    jam_jamdate.voting_start_date,
                    jam_jamdate.time_zone
            FROM jam_jam
            INNER JOIN jam_jamdate ON jam_jam.id = jam_jamdate.jam_id
            JOIN jam_jamcolor ON jam_jam.id = jam_jamcolor.jam_id
            '''

    _href = '/jam/jam-list.html'

    def get(self, request, **kwargs):
        jams = Jam.objects.raw(self._query)
        jamCards = [JamCard(jam) for jam in jams]
        return render(request, self._href, context={'jamCards': jamCards})


class JamParticipate(View):

    @staticmethod
    def get(request, **kwargs):
        user = request.user
        data = {'url': None}
        if user.is_authenticated:
            jamObject = Jam.objects.get(name__exact=kwargs['jamName'])
            if IsParticipant(user, jamObject):
                Participant.objects.get(user=user, jam=jamObject).delete()
            else:
                participant = Participant.objects.create(user=user,
                                                         jam=jamObject)
                participant.save()
            return JsonResponse({'message':'message'})
        else:
            data['url'] = redirect('login').url
            return JsonResponse(data)

class JamBlockControlView(View):

    def get(self, request, jamName):
        user = request.user
        jam = None
        data = {
            'url': None,
            'theme': None,
            'date': None,
            'isAuthor': False,
            'isParticipant': False,
            'color': None,
        }
        try:
            jam = Jam.objects.get(name=jamName)
        except ObjectDoesNotExist:
            print('jam not found')
        if jam is None:
            data['url'] = redirect('jamList').url
        else:
            data = self.AddDateToContext(jam, data)
            if not data['date']:
                data['theme'] = jam.theme
            if user.is_authenticated:
                if jam.author == user:
                    data['isAuthor'] = True
                else:
                    data['isParticipant'] = IsParticipant(user, jam)
            data['color'] = model_to_dict(JamColor.objects.get(jam=jam))
        return JsonResponse(data)

    @staticmethod
    def AddDateToContext(jam, context):
        jamDate = JamDate.objects.get(jam=jam)
        localStartDate = LocalizeDate(jamDate.start_date,
                                      jamDate.time_zone)
        if localStartDate > GetCurrentDate():
            context['date'] = localStartDate
        return context






