from django.shortcuts import render, redirect
from django.views import View

from jam.models import Jam
from jam.utils import IsParticipant
from project.forms import JamProjectRegisterForm, ProjectColorForm
from project.models import Project, ProjectColor
from project.utils import GetRegisterProjectFormContext, ProjectFormSaver, GetParticipantProject


class ProjectRegisterView(View):

    @staticmethod
    def get(request, **kwargs):
        user = request.user
        if user.is_authenticated:
            jam = Jam.objects.get(name__exact=kwargs['jamName'])
            if not IsParticipant(user, jam):
                return redirect('jamPage', **kwargs)
            project = GetParticipantProject(user, kwargs['jamName'])
            if project is not None:
                return redirect('projectPage', project.name)
            context = GetRegisterProjectFormContext()
            return render(request, '/jam/jam-registration.html', context=context)
        else:
            return redirect('login')

    @staticmethod
    def post(request, **kwargs):
        form = JamProjectRegisterForm(request.POST, request.FILES)
        color = ProjectColorForm(request.POST)

        formSaver = ProjectFormSaver()
        formSaver.MainFormSave(form, request, **kwargs)
        formSaver.RelativeFormsSave([color])
        if formSaver.isFormsValidated:
            formSaver.SaveRelativeObjects()
            return redirect(f'/project/{formSaver.mainObject.name}/')
        else:
            context = GetRegisterProjectFormContext(form, color)
            return render(request, '/jam/jam-registration.html', context=context)

class ProjectPageView(View):

    def get(self, request, **kwargs):
        project = Project.objects.get(name__exact=kwargs['projectName'])
        color = ProjectColor.objects.get(project=project)
        participant = project.participant.user
        context = {
            'project': project,
            'color': color,
            'participant': participant
        }
        return render(request, '/jam/project-page.html', context=context)