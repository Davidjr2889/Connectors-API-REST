from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework import routers
from .views import XlsViewSet

app_name = 'Xls'

router = routers.SimpleRouter()
router.register('', XlsViewSet, basename='xls')

urlpatterns = [
    path('', include(router.urls)),
]