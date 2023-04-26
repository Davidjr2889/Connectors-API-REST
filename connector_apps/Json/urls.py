from django.urls import path, include
from .views import JsonViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register('', JsonViewSet, basename='json')

app_name='Json'

urlpatterns =[

    path('', include(router.urls)),

]