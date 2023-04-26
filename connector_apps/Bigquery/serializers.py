from rest_framework import serializers
from .models import BigQueryModel

class BigQuerySerializer(serializers.ModelSerializer):
    class Meta:
            
        model = BigQueryModel
        fields = '__all__'
    