from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404

import pandas as pd
import json
#import pandas_gbq

from google.cloud import bigquery
from google.oauth2 import service_account

from .models import BigQueryModel
from .serializers import BigQuerySerializer

class BigQueryViewSet(viewsets.ModelViewSet):
    queryset = BigQueryModel.objects.all()

    def get_queryset(self):
        queryset = BigQueryModel.objects.all()
        return queryset
    
    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset,pk=pk)
        return obj
    
    def get_serializer_class(self,*args,**kwargs):
        return BigQuerySerializer
    
    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        file = request.FILES['file']
        file_name = str(file)
        
        pk = serializer.data['id']
        file = serializer.data['file']
        dataset = serializer.data['dataset']
        table = serializer.data['table']
        where = serializer.data['where']

        print(f'{pk},{file},{dataset},{table},{where}')
        


        SCOPES = [
            'https://www.googleapis.com/auth/cloud-platform'
        ]

        credentials = service_account.Credentials.from_service_account_file(filename=f'media/BigQuery/'+file_name,
                                                                            scopes=SCOPES)

        query = (f'select * from {dataset}.{table}')

        df = pd.read_gbq(credentials=credentials, query=query)
        print(df)

        return Response(serializer.data)
    
    @action(detail=True,methods=['GET'])
    def my_post(self,request, pk=None):

        queryset = BigQueryModel.objects.latest('id')
        with open('csv_tojson.json') as m_json:
            dados = json.load(m_json)
            
            return Response(dados)
        return Response({'msg':'blank'})
    
    @action(detail=True, methods=['GET'])
    def comunicator(self,request, pk=None):
        
        queryset = BigQueryModel.objects.latest('id')
        
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

