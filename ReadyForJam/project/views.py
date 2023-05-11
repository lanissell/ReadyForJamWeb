from django.shortcuts import render, redirect
from django.views import View

from jam.utils import ProjectFormSaver
from project.forms import JamProjectRegisterForm, ProjectColorForm
from project.utils import GetRegisterProjectFormContext


class ProjectRegisterView(View):

    @staticmethod
    def get(request, **kwargs):
        user = request.user
        if user.is_authenticated:
            context = GetRegisterProjectFormContext()
            return render(request, '/jam/jam-registration.html', context=context)
        else:
            return redirect('login')

    @staticmethod
    def post(request, **kwargs):
        form = JamProjectRegisterForm(request.POST, request.FILES)
        color = ProjectColorForm(request.POST)

        formSaver = ProjectFormSaver()
        formSaver.MainFormSave(form, request)
        formSaver.RelativeFormsSave([color])
        if formSaver.isFormsValidated:
            formSaver.SaveRelativeObjects()
            return redirect(f'../../jam/{formSaver.mainObject.name}/')
        else:
            context = GetRegisterProjectFormContext(form, color)
            return render(request, '/jam/jam-registration.html', context=context)
