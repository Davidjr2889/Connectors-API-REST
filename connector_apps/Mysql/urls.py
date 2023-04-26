from django.urls import path, include
from .views import MySqlViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', MySqlViewSet, basename='mysql')



app_name = 'Mysql'

urlpatterns = [
    path('', include(router.urls)),
]