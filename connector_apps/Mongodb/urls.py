from django.urls import path, include
from rest_framework import routers
from .views import MongoDbViewSet

app_name = 'Mongodb'

router = routers.SimpleRouter()
router.register('', MongoDbViewSet, basename='Mongodb')

urlpatterns = [
    path('', include(router.urls)),
]