from abc import ABC, abstractmethod

import os
from urllib.parse import urljoin

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class CustomStorage(FileSystemStorage):

    location = os.path.join(settings.MEDIA_ROOT, "django_ckeditor_5")
    base_url = urljoin(settings.MEDIA_URL, "django_ckeditor_5/")


class BasicHtmlAttrs:
    inputFieldAttrs = \
        {'class': 'registration__item-input'}

    colorFieldAttrs = \
        {'type': 'color', 'value': '#525252', 'class':'registration__color-input'}

class BaseFormSaver(ABC):

    def __init__(self):
        self.isFormsValidated = True
        self.mainObject = None
        self._objectsToSave = []

    @abstractmethod
    def MainFormSave(self, form, request):
        pass

    def RelativeFormsSave(self, forms):
        if not self.isFormsValidated \
                or self.mainObject is None:
            return
        for form in forms:
            if form.is_valid():
                relativeObject = form.save(commit=False)
                self._SetFK(relativeObject)
                self._objectsToSave.append(relativeObject)
            else:
                self.isFormsValidated = False
                return

    @abstractmethod
    def _SetFK(self, relativeObject):
        pass

    def SaveRelativeObjects(self):
        for obj in self._objectsToSave:
            obj.save()


