import json
from urllib.request import urlopen

import pytz
from tzlocal import get_localzone_name
from datetime import datetime
from jam.forms import JamRegistrationForm, JamDateForm, JamColorForm, JamCriteriaFormSet
from jam.models import Participant, JamCriteria

def GetJamFormContext(mainForm=None, dataForm=None,
                      colorForm=None, criteriaForm=None):
    if mainForm is None:
        mainForm = JamRegistrationForm()
    if not dataForm:
        dataForm = JamDateForm()
    if not colorForm:
        colorForm = JamColorForm()
    if not criteriaForm:
        criteriaForm = JamCriteriaFormSet(queryset=JamCriteria.objects.none())

    context = {
        'form': mainForm,
        'date': dataForm,
        'color': colorForm,
        'formSet': criteriaForm,
        'title': 'Создание джема',
        'btnName': 'Создать'}

    return context

def LocalizeDate(dateString:str, dateTimeZone:str):
    date = datetime.strptime(dateString, '%Y-%m-%dT%H:%M')
    tz = pytz.timezone(dateTimeZone)
    date = tz.localize(date)
    currentTz = get_localzone_name()
    date = date.astimezone(pytz.timezone(currentTz))
    return date

def GetCurrentDate():
    res = urlopen('https://worldtimeapi.org/api/ip')
    result = json.loads(res.read().strip().decode('utf-8'))
    date = datetime.strptime(result.get('datetime'), '%Y-%m-%dT%H:%M:%S.%f%z')
    return date

class JamCard:
    __id = 0

    def __init__(self, jam):
        self.__id = jam.id
        self.title = jam.name
        self.photo = '/media/' + str(jam.avatar)
        self.date = self.DateFormat(jam.startDate, jam.timeZone)
        self.author = jam.author
        self.color = jam.backgroundColor
        self.participantQuantity = self.CountParticipant()

    def CountParticipant(self):
        return Participant.objects.filter(jam_id__exact=self.__id).count()

    @staticmethod
    def DateFormat(dateString: str, dateTimeZone:str):
        date = LocalizeDate(dateString, dateTimeZone)
        return date.date().strftime('%d.%m.%Y')



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

    def DateFormSave(self, form:JamDateForm):
        if form.is_valid():
            newObject = form.save(commit=False)
            newObject.jam = self.jamObject
            newObject.timeZone = get_localzone_name()
            self.__allRelativeObjects.append(newObject)


    def FormsetSaver(self, formset, jam=None):
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


class JamPageControlBlock:

    @staticmethod
    def GetAuthorBlock(jamName, jamColor):
        block = f"""
        <div class="jam-block__form">
            <button type="button" class="jam-block__button"
                    style="background-color: {jamColor.formColor};
                    color: {jamColor.mainTextColor}"
                    onclick="window.location.href='/jam/{jamName}/update'">
                <div class="button-block__link">РЕДАКТИРОВАТЬ</div>
            </button>
            <button type="button" class="jam-block__button"
                    style="background-color: {jamColor.formColor};
                            color: {jamColor.mainTextColor}"
                    onclick="window.location.href='/jam/{jamName}/delete'">
                <div class="button-block__link">УДАЛИТЬ</div>
           </button>
        </div>"""
        return block

    @staticmethod
    def GetUserBlock(jamColor, href):
        block = f"""
        <div class="jam-block__form">
            <button type="button" class="jam-block__button"
                    style="background-color: { jamColor.formColor };
                    color: { jamColor.mainTextColor };"
                    onclick="window.location.href='{href}'">                 
                <div class="button-block__link">УЧАВСТВОВАТЬ</div>
            </button>
        </div>"""
        return block
