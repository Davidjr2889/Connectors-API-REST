from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import MongoDB_Model
from .serializers import MongoDB_Serializer

from django.shortcuts import get_object_or_404

import pandas as pd
import json

import pymongo
from pymongo import MongoClient



class MongoDbViewSet(viewsets.ModelViewSet):
    query = MongoDB_Model.objects.all()
    
    def get_queryset(self):
        queryset = MongoDB_Model.objects.all()
        return queryset
    
    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset,pk=pk)
        return obj
    
    def get_serializer_class(self):
        return MongoDB_Serializer
    
    def perform_create(self, serializer):
        serializer.save()
    
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer) 

        pk = serializer.data['id']
        username = serializer.data['username']
        password = serializer.data['password']
        database = serializer.data['data_base']            
        cluster = serializer.data['cluster_address']
        table = serializer.data['table_mongo']
        
        
        client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@{cluster}/{database}")

        def find_all():
            query = (f'SELECT*FROM {table};')
            df = pd.read_sql_query(query,client)
            return df
        
        with open(f'mongodb{pk}.json','w') as m_json:
            m_json.write("")
            m_json.close()
            
            
            
            sent_file = find_all().to_json(f'mongodb[{pk}.json', indent=1, orient='records')
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['GET'])
    def my_post(self,request,pk=None):
        
        with open(f'mongodb{pk}.json') as m_json:
            dados = json.load(m_json)
        return Response(dados, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def comunicator(self,request, pk=None):
        
        queryset = MongoDB_Model.objects.latest('id')
        
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