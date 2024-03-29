from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from login.views import UserLogout
from mainPage.views import MainPageView
from registration import views as regViews
from login import views as loginViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='mainPage'),
    path('register/', regViews.UserRegistrationView.as_view(), name='registration'),
    path('login/', loginViews.UserLoginView.as_view(), name='login'),
    path('jam/', include('jam.urls')),
    path('project/', include('project.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    re_path(r'^logout/$', UserLogout.as_view(), name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
