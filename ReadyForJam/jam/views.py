import json

from django.forms import model_to_dict
from django.http import JsonResponse

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views import View

from jam.forms import JamRegistrationForm, JamColorForm, JamDateForm, JamCriteriaFormSet
from jam.models import Jam, JamColor, JamDate, JamCriteria, Participant
from jam.utils import JamCard, JamFormSaver, GetJamFormContext, LocalizeDate, GetCurrentDate, \
    IsParticipant, IsAuthor
from project.models import Project, Vote


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

    def __init__ (self, **kwargs):
        self._context = {}
        super().__init__(**kwargs)

    @staticmethod
    def GetJam(name):
        return get_object_or_404(Jam, name__exact=name)

    def get(self, request, **kwargs):
        jam = None
        try:
            jam = self._context.get('jam')
            if jam is None:
                jam = self.GetJam(kwargs['jamName'])
                self._context['jam'] = jam
        except ObjectDoesNotExist:
            print('jam not found')
        if jam is not None:
            jamColor = JamColor.objects.get(jam=jam)
            self._context['jamColor'] = jamColor
            self._context['jamCount'] = JamCard.CountParticipant(jam.id)
            return render(request, '/jam/jam-page.html', context=self._context)
        else:
            return redirect('jamList')

class JamProjectsPageView(JamPageView):

    def get(self, request, **kwargs):
        jam = self.GetJam(kwargs['jamName'])
        self._context['jam'] = jam
        projects = Project.objects.filter(participant__jam=jam)
        if len(projects) == 0:
            projects = 'No projects'
        self._context['cards'] = projects
        return super().get(request, **kwargs)

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

    _template = '/jam/jam-list.html'

    def get(self, request, **kwargs):
        jams = Jam.objects.raw(self._query)
        jamCards = [JamCard(jam) for jam in jams]
        jamCards = sorted(jamCards, key=lambda c: c.participantQuantity, reverse=True)
        return render(request, self._template, context={'jamCards': jamCards})

    def post(self, request):
        isQuantityReverse = json.loads(request.body).get('is_quantity_reverse')
        jams = Jam.objects.raw(self._query)
        jamCards = sorted([JamCard(jam) for jam in jams],
                          key=lambda c: c.participantQuantity,
                          reverse=isQuantityReverse)
        cards = render_to_string(
            template_name = self._template,
            context= {'jamCards': jamCards},
            request=request
        )
        print(isQuantityReverse)
        json_sort = {"sort_by_choice": cards}
        return JsonResponse(data=json_sort, safe=False)


class JamParticipate(View):

    @staticmethod
    def get(request, **kwargs):
        user = request.user
        data = {'url': None}
        if user.is_authenticated:
            jamObject = Jam.objects.get(name__exact=kwargs['jamName'])
            if IsAuthor(user, jamObject):
                return JsonResponse({})
            if IsParticipant(user, jamObject):
                Participant.objects.get(user=user, jam=jamObject).delete()
            else:
                participant = Participant.objects.create(user=user,
                                                         jam=jamObject)
                participant.save()
            return JsonResponse({})
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


class JamCriteriaView(View):

    def get(self, request, **kwargs):
        jam = get_object_or_404(Jam, name=kwargs['jamName'])
        criteria = JamCriteria.objects.filter(jam=jam)
        projects = Project.objects.filter(participant__jam=jam)
        data = {}
        for project in projects:
            projectCriteria = []
            for row in criteria:
                projectCriteria.append(json.dumps(CriteriaRow(row, project).__dict__))
            data[project.name] = projectCriteria
        return JsonResponse(data, safe=False)


class CriteriaRow:

    def __init__(self, criteria, project):
        self.name = criteria.name
        self.position = 0
        self.count = self.GetVoteCount(project.name)

    def GetVoteCount(self, projectName):
         votes = Vote.objects.filter(criteria__name=self.name,
                                     project__name=projectName)
         return len(votes)