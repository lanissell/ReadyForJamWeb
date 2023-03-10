from django.contrib import admin
from django.urls import path, include

import authorization


urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', include('authorization.urls')),
]
