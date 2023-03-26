from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from registration import views as regViews
from login import views as loginViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', regViews.UserRegistrationView.as_view(), name='registration'),
    path('login/', loginViews.UserLoginView.as_view(), name='login'),
    path('jam/', include('jam.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
