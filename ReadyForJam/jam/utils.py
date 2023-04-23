from datetime import datetime


from jam.forms import JamRegistrationForm, JamDateForm, JamColorForm, JamCriteriaFormSet
from jam.models import Participant

def GetJamContext(mainForm = None, dataForm = None,
                  colorForm = None, criteriaForm = None):
    if mainForm is None:
        mainForm = JamRegistrationForm()
    if not dataForm:
        dataForm = JamDateForm()
    if not colorForm:
        colorForm = JamColorForm()
    if not criteriaForm:
        criteriaForm = JamCriteriaFormSet()

    context = {
        'form': mainForm,
        'date': dataForm,
        'color': colorForm,
        'formSet': criteriaForm,
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
        self.__allRelativeObjects = []

    def MainFormSave(self, form, request):
        if form.is_valid() and request.user.is_authenticated:
            self.jamObject = form.save(commit=False)
            self.jamObject.author = request.user
            self.__allRelativeObjects.append(self.jamObject)
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
                self.__allRelativeObjects.append(newObject)
            else:
                self.isFormsValidated = False
                return

    def FormsetSaver (self, formset, jam = None):
        if jam is None:
            jam = self.jamObject
        if formset.is_valid():
            criteria = formset.save(commit=False)
            for c in criteria:
                c.jam = jam
                self.__allRelativeObjects.append(c)
        else:
            self.isFormsValidated = False

    def SaveRelativeObjects(self):
        for obj in self.__allRelativeObjects:
            obj.save()
