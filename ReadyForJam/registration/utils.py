from .forms import UserPhotoForm, UserDataForm, UserRegistrationForm
from registration.models import UserRight, Right

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

class UserFormSaver:

    @staticmethod
    def UserPhotoSave(photoForm, userObject):
        if photoForm.is_valid():
            photo = photoForm.save(commit=False)
            photo.user = userObject
            photo.save()

    @staticmethod
    def UserDataSave(dataForm, userObject):
        if dataForm.is_valid():
            photo = dataForm.save(commit=False)
            photo.user = userObject
            photo.save()

    @staticmethod
    def SetUserRight(userObject, rightId):
        userRight = UserRight()
        userRight.user = userObject
        right = Right.objects.get(pk=rightId)
        userRight.right = right
        userRight.save()

