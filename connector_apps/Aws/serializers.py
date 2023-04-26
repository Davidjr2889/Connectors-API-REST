from rest_framework import serializers
from .models import Aws_Model

class Aws_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Aws_Model
        fields = '__all__'