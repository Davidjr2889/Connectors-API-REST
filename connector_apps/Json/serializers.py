from rest_framework import serializers
from .models import Json_Model

class Json_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Json_Model
        fields = '__all__'