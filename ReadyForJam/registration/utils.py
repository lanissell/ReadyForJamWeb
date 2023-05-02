from .forms import UserPhotoForm, UserDataForm, UserRegistrationForm
from registration.models import UserRight, Right

class UserFormSaver:

    def __init__(self):
        self.isFormsValidated = True
        self.userObject = None
        self.objectsToSave = []

    def MainFormSave(self, form):
        if form.is_valid():
            self.userObject = form.save(commit=False)
            self.objectsToSave.append(self.userObject)
        else:
            self.isFormsValidated = False

    def RelativeFormSave(self, form):
        if not self.isFormsValidated \
                or self.userObject is None:
            return
        if form.is_valid():
            relativeObject = form.save(commit=False)
            relativeObject.user = self.userObject
            self.objectsToSave.append(relativeObject)
        else:
            self.isFormsValidated = False

    def SetCurrentUserRight(self, rightId):
        userRight = UserRight(user=self.userObject)
        right = Right.objects.get(pk=rightId)
        userRight.right = right
        self.objectsToSave.append(userRight)



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

