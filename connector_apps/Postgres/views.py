from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from django.core.files.storage import FileSystemStorage

from django.shortcuts import get_object_or_404

from .models import Postgres_Model
from .serializers import Postgres_Serializer

import pandas as pd
import json

import psycopg2


class PostgresViewSet(viewsets.ModelViewSet):
    queryset = Postgres_Model.objects.all()
    
    def get_queryset(self):
        queryset = Postgres_Model.objects.all()
        return queryset
    
    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset,pk=pk)
        return obj
    
    def get_serializer_class(self):
        return Postgres_Serializer
    
    def perform_create(self, serializer):
        serializer.save()
            
    
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        pk = serializer.data['id']
        host_1 = serializer.data['host']
        user_1 = serializer.data['user']
        password_1 = serializer.data['password']
        database_1 = serializer.data['database']
        port = serializer.data['port']
        table = serializer.data['table_postgres']
        
        print(pk)
        print(host_1)
        print(user_1)
        print(password_1)
        print(database_1)
                            
        conn = psycopg2.connect(
            user=user_1, 
            password=password_1,
            dbname=database_1,
            host = host_1,
            port=port
        )
        cur = conn.cursor()
        def find_all():
            cur.execute(f'SELECT*FROM {table};')
        
            query = (f'SELECT*FROM {table};')
            df = pd.read_sql_query(query,conn)
            return df
        
        
        with open(f'postgres{pk}.json','w') as data_json:
            data_json.write("")
            data_json.close()
           
            sent_file = find_all().to_json(f'postgres{pk}.json', indent=1, orient='records')
                        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['GET'])
    def my_post(self, request, pk=None):
        with open(f'postgres{pk}.json') as m_json:
            dados = json.load(m_json)
        return Response(dados, status=status.HTTP_200_OK)
            
    @action(detail=True, methods=['GET'])
    def comunicator(self,request, pk=None):
        
        queryset = Postgres_Model.objects.latest('id')
        
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