from rest_framework import serializers
from .models import MariaDb_Model

class MariaDb_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MariaDb_Model
        fields = '__all__'