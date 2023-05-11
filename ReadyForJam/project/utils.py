from globalUtils import BaseFormSaver
from jam.models import Participant
from project.forms import JamProjectRegisterForm, ProjectColorForm
from project.models import Project


def GetRegisterProjectFormContext(mainForm=None, colorForm=None, ):
    if mainForm is None:
        mainForm = JamProjectRegisterForm()
    if not colorForm:
        colorForm = ProjectColorForm()
    context = {
        'form': mainForm,
        'color': colorForm,
        'title': 'Добавление проекта',
        'btnName': 'Добавить'}
    return context

def GetParticipantProject(user, jamName):
    project = Project.objects.filter(participant__user_id=user.id,
                                     participant__jam__name__exact=jamName)
    if project.count() == 0:
        return None
    return project[0]


class ProjectFormSaver(BaseFormSaver):
    def _SetFK(self, relativeObject):
        relativeObject.project = self.mainObject

    def MainFormSave(self, form, request, **kwargs):
        if form.is_valid() and request.user.is_authenticated:
            self.mainObject = form.save(commit=False)
            participant = Participant.objects.raw(
                f'''SELECT jam_participant.id 
                    FROM jam_participant
                    JOIN jam_jam ON jam_participant.jam_id = jam_jam.id
                    WHERE jam_jam.name = '{kwargs['jamName']}' AND 
                          jam_participant.user_id = {request.user.id}'''
            )
            self.mainObject.participant_id = participant[0].id
            self._objectsToSave.append(self.mainObject)
        else:
            self.isFormsValidated = False