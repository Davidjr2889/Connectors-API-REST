from django.urls import path, include
from .views import PostgresViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', PostgresViewSet, basename='Postgres')

app_name = 'Postgres'

urlpatterns = [
    path('', include(router.urls))
]