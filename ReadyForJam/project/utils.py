from project.forms import JamProjectRegisterForm, ProjectColorForm


def GetRegisterProjectFormContext(mainForm=None, colorForm=None, ):
    if mainForm is None:
        mainForm = JamProjectRegisterForm()
    if not colorForm:
        colorForm = ProjectColorForm()
    context = {
        'form': mainForm,
        'color': colorForm,
        'title': 'Добавление проекта',
        'btnName': 'Добавить'}
    return context