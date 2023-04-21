
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View


from jam.forms import JamRegistrationForm, JamColorForm, JamDateForm, JamCriteriaFormSet
from jam.models import Jam, JamColor, JamDate
from jam.utils import JamCard, JamFormSaver, GetJamContext


class JamRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        if request.user.is_authenticated:
            context = GetJamContext()
            return render(request, '../templates/jam/jam-registration.html', context=context)
        else:
            return redirect('login')

    @staticmethod
    def post(request, **kwargs):
        form = JamRegistrationForm(request.POST, request.FILES)
        color = JamColorForm(request.POST)
        date = JamDateForm(request.POST)
        formSaver = JamFormSaver()
        formSaver.MainFormSave(form, request)
        formSaver.RelativeFormsSave([color, date])
        if formSaver.isFormsValidated:
            return redirect(f'../../jam/{formSaver.jamObject.name}')
        else:
            context = GetJamContext(form, color, date)
            return render(request, '../templates/jam/jam-registration.html', context=context)


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
                colorObject = JamColor.objects.get(jam=jamObject)
                dateObject = JamDate.objects.get(jam=jamObject)
                jam = JamRegistrationForm(instance=jamObject)
                color = JamColorForm(instance=colorObject)
                date = JamDateForm(instance=dateObject)
                context = GetJamContext(jam, color, date)
                context.update(self.baseContext)
                return render(request, '../templates/jam/jam-registration.html', context=context)
            else:
                return redirect('jamList')
        else:
            return redirect('login')

    def post(self, request, **kwargs):
        jamObject = Jam.objects.get(name__exact=kwargs['jamName'])

        jam = JamRegistrationForm(request.POST, request.FILES,
                                  instance=jamObject)
        color = JamColorForm(request.POST)
        date = JamDateForm(request.POST)

        if jam.is_valid() and color.is_valid() and date.is_valid():
            Jam.objects.update_or_create(id=jamObject.id,
                                         defaults=jam.cleaned_data)
            JamColor.objects.update_or_create(jam=jamObject,
                                              defaults=color.cleaned_data)
            JamDate.objects.update_or_create(jam=jamObject,
                                             defaults=date.cleaned_data)
            return redirect(f'../../jam/{jamObject.name}')
        else:
            context = GetJamContext(jam, color, date)
            context.update(self.baseContext)
            return render(request, '../templates/jam/jam-registration.html', context=context)

class JamPageView(View):

    @staticmethod
    def get(request, jamName ,**kwargs):
        jam = None
        context = {}
        try:
            jam = Jam.objects.get(name = jamName)
        except ObjectDoesNotExist:
            print('jam not found')
        if jam is not None:
            jamColor = JamColor.objects.get(jam = jam)
            jamDate = JamDate.objects.get(jam = jam)
            context['jam'] = jam
            context['jamColor'] = jamColor
            context['jameDate'] = jamDate
        return render(request, '../templates/jam/jam-page.html', context=context)

class JamDeleteView(View):

    @staticmethod
    def get(request, **kwargs):
        user = request.user
        if user.is_authenticated:
            jamObject = Jam.objects.get(name__exact=kwargs['jamName'])
            if jamObject.author.id == user.id:
                jamObject.delete()
            return redirect('jamList')
        else:
            return redirect('login')

class JamListView(View):
    @staticmethod
    def get(request, **kwargs):
        jams = Jam.objects.raw('''
            SELECT  jam_jam.id, 
                    jam_jam.name, 
                    main.jam_jam.avatar,
                    main.jam_jamcolor.backgroundColor,
                    main.jam_jamdate.startDate
            FROM main.jam_jam
            JOIN main.jam_jamdate ON (jam_jam.id = jam_jamdate.jam_id)
            JOIN main.jam_jamcolor ON (jam_jam.id = jam_jamcolor.jam_id)
            ''')
        jamCards = [JamCard(jam) for jam in jams]
        return render(request, '../templates/jam/jam-list.html', context={'jamCards': jamCards})


