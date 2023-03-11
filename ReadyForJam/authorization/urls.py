from django.urls import path

from authorization import views

urlpatterns = [
    path('', views.UserRegistrationView.as_view()),
    path('login/', views.UserLoginView.as_view()),
]
