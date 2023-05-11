from abc import ABC, abstractmethod


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


