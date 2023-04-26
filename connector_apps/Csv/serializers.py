from rest_framework import serializers
from .models import Csv_Model

class Csv_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Csv_Model
        fields = '__all__'