
from django.contrib import admin
from django.urls import path, include

import wbapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wbapp.urls'))
]
