from django.shortcuts import render, redirect
from django.views import View

from jam.forms import JamRegistrationForm


class JamRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        context = {'form': JamRegistrationForm}
        return render(request, '../templates/jam/form-template.html', context=context)

    @staticmethod
    def post(request, **kwargs):
        form = JamRegistrationForm(request.POST)
        context = {}
        if form.is_valid():
            jam = form.save(commit=True)
            context['jam'] = jam
            return render(request, '../templates/jam/jam-page.html', context=context)
        else:
            return redirect('jamRegister')