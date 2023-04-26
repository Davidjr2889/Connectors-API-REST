from rest_framework import serializers
from .models import Xls_Model

class Xls_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Xls_Model
        fields = '__all__'