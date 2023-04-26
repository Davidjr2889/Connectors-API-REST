from django.urls import path,include
from rest_framework.routers import SimpleRouter
from rest_framework import routers
from .views import XlsxViewSet

app_name = 'xlsx'

router = routers.SimpleRouter()
router.register('', XlsxViewSet, basename='xlsx')

urlpatterns = [
    path('', include(router.urls))
]