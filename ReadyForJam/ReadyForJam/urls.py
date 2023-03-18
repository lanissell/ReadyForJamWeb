from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from registration import views as regViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', regViews.UserRegistrationView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
