from rest_framework import serializers
from .models import Html_Model

class Html_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Html_Model
        fields = '__all__'