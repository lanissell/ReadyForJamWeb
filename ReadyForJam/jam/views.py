
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View


from jam.forms import JamRegistrationForm, JamColorForm, JamDateForm, JamCriteriaFormSet
from jam.models import Jam, JamColor, JamDate
from jam.utils import JamCard, JamFormSaver, GetJamContext


class JamRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        context = GetJamContext()
        return render(request, '../templates/jam/form-template.html', context=context)

    @staticmethod
    def post(request, **kwargs):
        form = JamRegistrationForm(request.POST, request.FILES)
        color = JamColorForm(request.POST)
        date = JamDateForm(request.POST)
        formSaver = JamFormSaver()
        formSaver.MainFormSave(form)
        formSaver.RelativeFormsSave([color, date])
        if formSaver.isFormsValidated:
            return redirect(f'../../jam/{formSaver.jamObject.name}')
        else:
            context = GetJamContext(form, color, date)
            return render(request, '../templates/jam/form-template.html', context=context)


class JamUpdateView(View):

    def get(self, request, **kwargs):
        jamObject = Jam.objects.get(name__exact=kwargs['jamName'])
        colorObject = JamColor.objects.get(jam=jamObject)
        dateObject = JamDate.objects.get(jam=jamObject)

        jam = JamRegistrationForm(instance=jamObject)
        color = JamColorForm(instance=colorObject)
        date = JamDateForm(instance=dateObject)
        context = GetJamContext(jam, color, date)
        return render(request, '../templates/jam/form-template.html', context=context)


    def post(self, request, **kwargs):
        isValidated = True

        jamObject = Jam.objects.get(name__exact=kwargs['jamName'])
        colorObject = JamColor.objects.get(jam=jamObject)
        dateObject = JamDate.objects.get(jam=jamObject)

        jam = JamRegistrationForm(request.POST, request.FILES,
                                  instance=jamObject)
        color = JamColorForm(request.POST,
                             instance=colorObject)
        date = JamDateForm(request.POST,
                           instance=dateObject)

        if jam.is_valid():
            jamObject.name = jam.cleaned_data['name']
            jamObject.theme = jam.cleaned_data['theme']
            jamObject.content = jam.cleaned_data['content']
            jamObject.avatar = jam.cleaned_data['avatar']
        else:
            isValidated = False

        if color.is_valid() and isValidated:
            #color.update(**color.cleaned_data)
            colorObject.backgroundColor =  color.cleaned_data['backgroundColor']
            colorObject.formColor =  color.cleaned_data['formColor']
            colorObject.mainTextColor =  color.cleaned_data['mainTextColor']
        else:
            isValidated = False

        if date.is_valid() and isValidated:
            dateObject.startDate = date.cleaned_data['startDate']
            dateObject.votingStartDate = date.cleaned_data['votingStartDate']
            dateObject.votingEndDate = date.cleaned_data['votingEndDate']
        else:
            isValidated = False

        if isValidated:
            jamObject.save()
            colorObject.save()
            dateObject.save()
            return redirect(f'../../jam/{jamObject.name}')
        else:
            context = GetJamContext(jam, color, date)
            return render(request, '../templates/jam/form-template.html', context=context)

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

    def get(self, request, **kwargs):
        jamObject = Jam.objects.get(name__exact=kwargs['jamName'])
        jamObject.delete()
        return redirect('jamList')

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
        jamCards = [JamCard(jam.id,
                            jam.name,
                            jam.avatar,
                            jam.startDate,
                            jam.backgroundColor)
                    for jam in jams]
        return render(request, '../templates/jam/jam-list.html', context={'jamCards': jamCards})


