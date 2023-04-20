from datetime import datetime

from django.contrib.auth.models import User

from jam.forms import JamRegistrationForm, JamDateForm, JamColorForm
from jam.models import Participant

def GetJamContext(mainForm = None, dataForm = None, colorForm = None):
    if mainForm is None:
        mainForm = JamRegistrationForm()
    if not dataForm:
        dataForm = JamDateForm()
    if not colorForm:
        colorForm = JamColorForm()

    context = {
        'form': mainForm,
        'date': dataForm,
        'color': colorForm,
        'title': 'Создание джема',
        'btnName': 'Создать'}

    return context


class JamCard:

    __id = 0

    def __init__(self, jam):
        self.__id = jam.id
        self.title = jam.name
        self.photo = '/media/' + str(jam.avatar)
        self.date = self.DateFormat(jam.startDate)
        self.author = jam.author
        self.color = jam.backgroundColor
        self.participantQuantity = self.CountParticipant()

    def CountParticipant(self):
        return Participant.objects.filter(jam_id__exact=self.__id).count()

    @staticmethod
    def DateFormat(date:str):
        datePart = datetime.strptime(date.split('T')[0], "%Y-%m-%d")
        datePart = datePart.strftime("%d.%m.%Y")
        return datePart

class JamFormSaver:

    def __init__(self):
        self.isFormsValidated = True
        self.jamObject = None

    def MainFormSave(self, form, request):
        if form.is_valid() and request.user.is_authenticated:
            self.jamObject = form.save(commit=False)
            self.jamObject.author = request.user
            self.jamObject.save()
        else:
            self.isFormsValidated = False

    def RelativeFormsSave(self, forms):
        if not self.isFormsValidated \
                or self.jamObject is None:
            return
        for form in forms:
            if form.is_valid():
                newObject = form.save(commit=False)
                newObject.jam = self.jamObject
                newObject.save()
            else:
                self.isFormsValidated = False
                break



