from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from jam.models import Jam
from jam.utils import IsParticipant
from project.forms import JamProjectRegisterForm, ProjectColorForm
from project.models import Project, ProjectColor
from project.utils import GetRegisterProjectFormContext, ProjectFormSaver, GetParticipantProject, IsProjectAuthor, \
    GetProjectInstanceForm


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
            return redirect('projectPage', formSaver.mainObject.name)
        else:
            context = GetRegisterProjectFormContext(form, color)
            return render(request, '/jam/jam-registration.html', context=context)

class ProjectUpdateView(View):

    def get(self, request, **kwargs):
        user = request.user
        if user.is_authenticated:
            project = Project.objects.get(name__exact=kwargs['projectName'])
            if IsProjectAuthor(user, project):
                context = GetProjectInstanceForm(project)
                context['title'] = 'Изменение данных'
                context['btnName'] = 'Изменить'
                return render(request, '/jam/jam-registration.html/', context=context)
            else:
                return redirect('projectPage', **kwargs)
        else:
            return redirect('login')

    def post(self, request, **kwargs):
        project = Project.objects.get(name__exact=kwargs['projectName'])
        form = JamProjectRegisterForm(request.POST, request.FILES, instance=project)
        color = ProjectColorForm(request.POST)
        if form.is_valid() and color.is_valid():
            Project.objects.update_or_create(id=project.id, defaults=form.cleaned_data)
            ProjectColor.objects.update_or_create(project=project, defaults=color.cleaned_data)
            return redirect(f'/project/{form.cleaned_data["name"]}')
        else:
            context = GetRegisterProjectFormContext(form, color)
            return render(request, '/jam/jam-registration.html', context=context)


class ProjectPageView(View):

    def get(self, request, **kwargs):
        project = Project.objects.get(name__exact=kwargs['projectName'])
        color = ProjectColor.objects.get(project=project)
        participant = project.participant
        context = {
            'project': project,
            'color': color,
            'participant': participant
        }
        return render(request, '/jam/project-page.html', context=context)

class ProjectControlBlockView(View):

    def get(self, request, **kwargs):
        user = request.user
        data = {
            'isAuthor': False,
            'projectColor': None,
            'jamName': None
        }
        project = Project.objects.get(name__exact=kwargs['projectName'])
        data['projectColor'] = model_to_dict(ProjectColor.objects.get(project=project))
        data['jamName'] = project.participant.jam.name
        if user.is_authenticated:
            data['isAuthor'] = IsProjectAuthor(user, project)
        return JsonResponse(data)
