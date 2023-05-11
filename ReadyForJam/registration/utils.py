from globalUtils import BaseFormSaver
from .forms import UserPhotoForm, UserDataForm, UserRegistrationForm
from registration.models import UserRight, Right

class UserFormSaver(BaseFormSaver):

    def _SetFK(self, relativeObject):
        relativeObject.user = self.mainObject

    def MainFormSave(self, form, request):
        if form.is_valid():
            self.mainObject = form.save(commit=False)
            self._objectsToSave.append(self.mainObject)
        else:
            self.isFormsValidated = False



    def SetCurrentUserRight(self, rightId):
        userRight = UserRight(user=self.mainObject)
        right = Right.objects.get(pk=rightId)
        userRight.right = right
        self._objectsToSave.append(userRight)



def GetRegisterFormContext(regForm = None, dataForm = None, photoForm = None):
    if regForm is None:
        regForm = UserRegistrationForm()
    if not dataForm:
        dataForm = UserDataForm()
    if not photoForm:
        photoForm = UserPhotoForm()
    context = {'form': regForm,
               'dataForm': dataForm,
               'photoForm': photoForm}
    return context

