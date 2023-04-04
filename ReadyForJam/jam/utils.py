from datetime import datetime

from jam.models import Participant


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
    def DateFormat(date:datetime):
        datePart = date.strftime('%d.%m.%y %H:%M')
        return datePart