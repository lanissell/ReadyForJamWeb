from datetime import datetime

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
    }
    return context


class JamCard:

    __id = 0

    def __init__(self, id, title, photo, date, color):
        self.__id = id
        self.title = title
        self.photo = '/media/' + str(photo)
        self.date = self.DateFormat(date)
        self.color = color
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

    def MainFormSave(self, form):
        if form.is_valid():
            self.jamObject = form.save(commit=True)
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



