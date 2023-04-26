from rest_framework import serializers
from .models import Xlsx_Model

class Xlsx_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Xlsx_Model
        fields = '__all__'