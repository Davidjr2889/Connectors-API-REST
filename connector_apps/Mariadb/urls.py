from django.urls import path, include
from rest_framework import routers
from .views import MariaDbViewSet

app_name = 'Mariadb'

router = routers.SimpleRouter()
router.register('', MariaDbViewSet, basename='Mariadb')

urlpatterns = [
    path('', include(router.urls)),
]
