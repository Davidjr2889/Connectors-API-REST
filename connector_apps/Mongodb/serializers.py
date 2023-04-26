from rest_framework import serializers
from .models import MongoDB_Model

class MongoDB_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MongoDB_Model
        fields = '__all__'