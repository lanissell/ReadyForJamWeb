from .forms import UserPhotoForm, UserDataForm, UserRegistrationForm
from registration.models import UserRight, Right

class UserFormSaver:

    def __init__(self):
        self.isFormsValidated = True
        self.userObject = None

    def MainFormSave(self, form):
        if form.is_valid():
            self.userObject = form.save(commit=True)
        else:
            self.isFormsValidated = False

    def RelativeFormSave(self, form):
        if not self.isFormsValidated \
                or self.userObject is None:
            return
        if form.is_valid():
            relativeObject = form.save(commit=False)
            relativeObject.user = self.userObject
            relativeObject.save()
        else:
            self.isFormsValidated = False

    def SetCurrentUserRight(self, rightId):
        self.SetUserRight(self.userObject, rightId)

    @staticmethod
    def SetUserRight(userObject, rightId):
        userRight = UserRight()
        userRight.user = userObject
        right = Right.objects.get(pk=rightId)
        userRight.right = right
        userRight.save()


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

