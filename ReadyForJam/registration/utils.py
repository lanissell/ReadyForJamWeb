
class BasicHtmlAttrs:

    inputFieldAttrs = attrs = {'class': 'registration__item-input'}


def CreateFormViewContext(pageTitle, action,
                          submitBtnText, form):
    context = {
        'pageTitle': pageTitle,
        'action': action,
        'submitBtnText': submitBtnText,
        'form': form
    }
    return context
