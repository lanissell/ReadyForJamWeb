from django.urls import re_path

from user.views import UserProfileView

urlpatterns = [
    re_path(r'^(?P<uid>\d+)/$', UserProfileView.as_view()),
]
