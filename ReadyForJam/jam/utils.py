import json

import pytz
import requests
from tzlocal import get_localzone_name
from datetime import datetime

from globalUtils import BaseFormSaver
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
    url = f'https://timezoneapi.io/api/timezone/?{get_localzone_name()}&token=aaZtuEvfxzbSelVoYmwh'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
    r = requests.get(url, headers=headers)
    result = json.loads(r.content)
    date = result.get('data').get('datetime').get('date_time_ymd')
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%f%z')
    return date



def IsParticipant(user, jam):
    participants = Participant.objects.raw(f'''
                            SELECT id, user_id
                            FROM jam_participant
                            WHERE jam_id = {jam.id}''')
    participantsList = [u.user_id for u in participants]
    if user.id in participantsList:
        return True
    else:
        return False

def IsAuthor(user, jam):
    if jam.author == user:
        return True
    else:
        return False

class JamCard:

    def __init__(self, jam):
        self.title = jam.name
        self.photo = '/media/' + str(jam.avatar)
        self.date = self.DateFormat(jam.start_date, jam.time_zone)
        self.author = jam.author.username
        self.color = jam.background_color
        self.participantQuantity = self.CountParticipant(jam.id)

    @staticmethod
    def CountParticipant(id):
        return Participant.objects.filter(jam_id__exact=id).count()

    @staticmethod
    def DateFormat(dateString: str, dateTimeZone:str):
        date = LocalizeDate(dateString, dateTimeZone)
        return date.date().strftime('%d.%m.%Y')



class JamFormSaver(BaseFormSaver):

    def MainFormSave(self, form, request):
        if form.is_valid() and request.user.is_authenticated:
            self.mainObject = form.save(commit=False)
            self.mainObject.author = request.user
            self._objectsToSave.append(self.mainObject)
        else:
            self.isFormsValidated = False

    def _SetFK(self, relativeObject):
        relativeObject.jam = self.mainObject

    def DateFormSave(self, form:JamDateForm):
        if form.is_valid():
            newObject = form.save(commit=False)
            newObject.jam = self.mainObject
            newObject.timeZone = get_localzone_name()
            self._objectsToSave.append(newObject)

    def FormsetSaver(self, formset, jam=None):
        if jam is None:
            jam = self.mainObject
        if formset.is_valid():
            criteria = formset.save(commit=False)
            for c in criteria:
                c.jam = jam
                self._objectsToSave.append(c)
        else:
            self.isFormsValidated = False


