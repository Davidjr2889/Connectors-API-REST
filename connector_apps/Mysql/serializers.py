from rest_framework import serializers
from .models import MySql_Model

class Mysql_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MySql_Model
        fields = '__all__'