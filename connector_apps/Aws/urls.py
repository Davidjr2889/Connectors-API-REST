from django.urls import path, include
from rest_framework import routers

from .views import AwsViewSet

app_name = 'Aws'

router = routers.SimpleRouter()
router.register('', AwsViewSet, basename='Aws')

urlpatterns = [
    path('', include(router.urls)),
]