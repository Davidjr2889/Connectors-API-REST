from django.urls import path, include
from rest_framework import routers
from .views import HtmlViewSet

router = routers.SimpleRouter()
router.register('', HtmlViewSet, basename='html')

app_name = 'Html'

urlpatterns = [
    
    path('', include(router.urls))
]