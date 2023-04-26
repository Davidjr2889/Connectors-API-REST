from django.urls import path, include
#from django.conf.urls import url

from .views import CsvViewSet

from rest_framework.routers import DefaultRouter
from rest_framework import routers

app_name = 'Csv'

router = routers.SimpleRouter()

router.register('', CsvViewSet, basename='Csv')

urlpatterns = [
    
    path('', include(router.urls)),
    
    
]