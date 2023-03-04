from django.contrib import admin
from django.urls import path
from registration.views import UserRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view())
]
