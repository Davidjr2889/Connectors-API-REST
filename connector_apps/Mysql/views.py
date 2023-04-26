from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import MySql_Model
from .serializers import Mysql_Serializer

import pandas as pd
import json

import mysql.connector

class MySqlViewSet(viewsets.ModelViewSet):
    
    queryset = MySql_Model.objects.all()
    
    def get_queryset(self):
        queryset = MySql_Model.objects.all()
        return queryset
    
    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset,pk=pk)
        return obj
    
    def get_serializer_class(self):
        return Mysql_Serializer
    
    def perform_create(self, serializer):
        serializer.save()    
    
    def create(self, request, *args, **kwargs):
                
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)
        
        
        host = serializer.data['host']
        user = serializer.data['username']
        password = serializer.data['password']
        database = serializer.data['database']
        table = serializer.data['table_mysql']
                            
        conn = mysql.connector.connect(
            host = host, 
            user=user, 
            password=password,
            database=database,
        )

        with open('mysql_tojson.json','w') as m_json:
            m_json.write("")
            m_json.close()
            
            df = pd.read_sql_table(table, conn)
            
            f = df.to_json('mysql_tojson.json', indent=1, orient='records')
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['GET'])
    def my_post(self, request, pk=None):
        with open('mysql_tojson.json') as m_json:
            dados = json.load(m_json)
        return Response(dados, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def comunicator(self,request, pk=None):
        
        queryset = MySql_Model.objects.latest('id')
        
        #print(request.POST)
        #print(request.META)
        vr =request.META['PATH_INFO']
        print(vr)
        rep = vr.replace("comunicator","my_post")
        print(rep)
        
        self.link = 'http://'+request.META['HTTP_HOST'] + rep
        
        
        #print('http://'+request.META['HTTP_HOST'] + request.META['PATH_INFO'])
        #print('teste')
        #print(link)
        
        
        return Response({'Message':self.link})
            