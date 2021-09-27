from django.urls import path
from . import views
from .views import CFSActiveList

urlpatterns = [
    path('', views.index),
    path('cfs/', CFSActiveList.as_view(), name='cfs'),
    path('cfslist/', views.cfsfeed)
]
