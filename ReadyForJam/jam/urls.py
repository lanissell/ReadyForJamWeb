from django.urls import path

import jam.views as jv
from project.views import ProjectRegisterView

urlpatterns = [
    path('register/', jv.JamRegistrationView.as_view(), name='jamRegister'),
    path('all/', jv.JamListView.as_view(), name='jamList'),
    path('<str:jamName>/', jv.JamPageView.as_view(), name='jamPage'),
    path('<str:jamName>/update/', jv.JamUpdateView.as_view(), name='jamUpdate'),
    path('<str:jamName>/delete/', jv.JamDeleteView.as_view(), name='jamDelete'),
    path('<str:jamName>/criteria/', jv.JamCriteriaView.as_view(), name='jamCriteria'),
    path('<str:jamName>/participate/', jv.JamParticipate.as_view(), name='participate'),
    path('<str:jamName>/blockControl/', jv.JamBlockControlView.as_view(), name='blockControl'),
    path('<str:jamName>/projectRegister/', ProjectRegisterView.as_view(), name='projectRegister'),
    path('<str:jamName>/projects/', jv.JamProjectsPageView.as_view(), name='projects'),
]
