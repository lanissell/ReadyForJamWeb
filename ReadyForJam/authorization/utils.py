def CreateAuthorViewContext(pageTitle, submitBtnText, changePageBtnText, changePageBtnUrl, form):
    context = {
        'pageTitle': pageTitle,
        'submitBtnText': submitBtnText,
        'changePageBtnText': changePageBtnText,
        'changePageBtnUrl': changePageBtnUrl,
        'form': form
    }
    return context
