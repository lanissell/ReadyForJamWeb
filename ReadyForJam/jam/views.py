from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View

from jam.forms import JamRegistrationForm, JamColorForm, JamDateForm
from jam.models import Jam, JamColor, JamDate


class JamRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        context = {'form': JamRegistrationForm}
        color = JamColorForm
        date = JamDateForm
        context['color'] = color
        context['date'] = date
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
