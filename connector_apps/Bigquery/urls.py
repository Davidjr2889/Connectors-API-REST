from django.urls import path, include
from .views import BigQueryViewSet
from rest_framework import routers

app_name = 'Bigquery'

router = routers.SimpleRouter()
router.register('', BigQueryViewSet, basename='Bigquery')

urlpatterns = [
    path('', include(router.urls)),
]