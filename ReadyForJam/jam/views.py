
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View

from jam.forms import JamRegistrationForm, JamColorForm, JamDateForm, JamCriteriaFormSet
from jam.models import Jam, JamColor, JamDate
from jam.utils import JamCard


class JamRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        context = {'form': JamRegistrationForm}
        color = JamColorForm
        date = JamDateForm
        context['color'] = color
        context['date'] = date
        context['formSet'] = JamCriteriaFormSet()
        return render(request, '../templates/jam/form-template.html', context=context)

    @staticmethod
    def post(request, **kwargs):
        form = JamRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            jam = form.save(commit=True)
            if jam.id is not None:
                jamColorForm = JamColorForm(request.POST)
                jamDateForm = JamDateForm(request.POST)
                if jamColorForm.is_valid():
                    jamColor = jamColorForm.save(commit=False)
                    jamColor.jam = jam
                    jamColor.save()
                else:
                    return redirect('jamRegister')
                if jamDateForm.is_valid():
                    jamDate = jamDateForm.save(commit=False)
                    jamDate.jam = jam
                    jamDate.save()
                else:
                    return redirect('jamRegister')
            return redirect(f'../../jam/{jam.name}')
        else:
            return redirect('jamRegister')

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


