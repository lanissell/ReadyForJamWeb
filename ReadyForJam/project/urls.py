from django.urls import path

from project.views import ProjectPageView, ProjectUpdateView, ProjectControlBlockView

urlpatterns = [
    path('<str:projectName>/', ProjectPageView.as_view(), name='projectPage'),
    path('<str:projectName>/update/', ProjectUpdateView.as_view(), name='update'),
    path('<str:projectName>/delete/', ProjectPageView.as_view(), name='delete'),
    path('<str:projectName>/blockControl/', ProjectControlBlockView.as_view(), name='projectControlBlock'),
]