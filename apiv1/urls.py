from django.urls import path, include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register('testdata', views.TestDataViewSet)

urlpatterns = [
    path('', include(routers.urls))
]