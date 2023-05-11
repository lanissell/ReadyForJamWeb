from django.urls import path

from project.views import ProjectPageView

urlpatterns = [
    path('<str:projectName>/', ProjectPageView.as_view(), name='projectPage'),
]