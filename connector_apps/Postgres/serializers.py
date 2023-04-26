from rest_framework import serializers
from .models import Postgres_Model

class Postgres_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Postgres_Model
        fields = '__all__'