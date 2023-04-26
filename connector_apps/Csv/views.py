from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Csv_Model
from .serializers import Csv_Serializer
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import AllowAny

from django.shortcuts import get_object_or_404

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework import status
import pandas as pd
import json

import re

import requests


class CsvViewSet(viewsets.ModelViewSet):
    queryset = Csv_Model.objects.all()
    serializer_class = Csv_Serializer
    
    def get_queryset(self):
        
        queryset = Csv_Model.objects.all()
        return queryset
    
    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset,pk=pk)
        return obj
    
    def get_serializer_class(self,*args,**kwargs):
        return Csv_Serializer
    
    def perform_create(self, serializer):
        serializer.save()
    
    def create(self,request,*args,**kwargs):                       
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        file = request.FILES['file']
        file_name = str(file)
    
        if file_name.endswith('.csv'):
            
            self.perform_create(serializer)
            
            print('###############################')
            print('###############################')

            print(serializer.data)
            print('###############################')
            print('###############################')

            

            sep = serializer.data['sep']
            delimiter = serializer.data['delimiter']
            skipinitialspace = serializer.data['skipinitialspace']
            nrows = serializer.data['nrows']
            keep_default_na = serializer.data['keep_default_na']
            verbose = serializer.data['verbose']
            skip_blank_lines = serializer.data['skip_blank_lines']
            infer_datetime_format = serializer.data['infer_datetime_format']
            keep_date_col = serializer.data['keep_date_col']
            cache_dates = serializer.data['cache_dates']
            iterator = serializer.data['iterator']
            thousands = serializer.data['thousands'] 
            decimal = serializer.data['decimal']
            lineterminator = serializer.data['lineterminator']
            quoting = serializer.data['quoting']
            doublequote = serializer.data['doublequote']
            escapechar = serializer.data['escapechar']
            comment = serializer.data['comment']
            encoding = serializer.data['encoding']
            storage_options = serializer.data['storage_options']
            
            
            print('###############################')
            if serializer.data['sep'] == '':
                sep = ','
            if serializer.data['delimiter'] == '':
                delimiter = None
            if serializer.data['skipinitialspace']  == '':
                skipinitialspace = False
            if serializer.data['nrows']  == '':
                nrows = None
            if serializer.data['keep_default_na']  == '':
                keep_default_na = True
            if serializer.data['verbose']  == '':
                verbose = False   
            if serializer.data['skip_blank_lines']  == '':
                skip_blank_lines = True
            if serializer.data['infer_datetime_format']  == '':
                infer_datetime_format = False  
            if serializer.data['keep_date_col']  == '':
                keep_date_col = False
            if serializer.data['cache_dates']  == '':
                cache_dates = True
            if serializer.data['iterator']  == '':
                iterator = False 
            if serializer.data['thousands']  == '':
                thousands = None
            if serializer.data['decimal']  == '':
                decimal = '.'
            if serializer.data['lineterminator']  == '':
                lineterminator = '\n'   
            if serializer.data['quoting']  == '':
                quoting = 0
            if serializer.data['doublequote']  == '':
                doublequote = True
            if serializer.data['escapechar']  == '':
                escapechar = None
            if serializer.data['comment']  == '':
                comment = None
            if serializer.data['encoding']  == '':
                encoding = None
            if serializer.data['storage_options']  == '':
                storage_options = None


            print('###############################')
            print('VALIDA TESTE UNITARIO SEP')
            print(sep)
            print('FIM VALIDA TESTE UNITARIO SEP')
            print('###############################')
            
            print('###############################')
            print('VALIDA TESTE UNITARIO skipinitialspace')
            print(skipinitialspace)
            print('FIM VALIDA TESTE UNITARIO skipinitialspace')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO nrows')
            print(nrows)
            print('FIM VALIDA TESTE UNITARIO nrows')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO keep_default_na')
            print(keep_default_na)
            print('FIM VALIDA TESTE UNITARIO keep_default_na')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO verbose')
            print(verbose)
            print('FIM VALIDA TESTE UNITARIO verbose')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO skip_blank_lines')
            print(skip_blank_lines)
            print('FIM VALIDA TESTE UNITARIO skip_blank_lines')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO infer_datetime_format')
            print(infer_datetime_format)
            print('FIM VALIDA TESTE UNITARIO infer_datetime_format')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO keep_date_col')
            print(keep_date_col)
            print('FIM VALIDA TESTE UNITARIO keep_date_col')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO cache_dates')
            print(cache_dates)
            print('FIM VALIDA TESTE UNITARIO cache_dates')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO iterator')
            print(iterator)
            print('FIM VALIDA TESTE UNITARIO iterator')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO thousands')
            print(thousands)
            print('FIM VALIDA TESTE UNITARIO thousands')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO decimal')
            print(decimal)
            print('FIM VALIDA TESTE UNITARIO decimal')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO lineterminator')
            print(lineterminator)
            print('FIM VALIDA TESTE UNITARIO lineterminator')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO quoting')
            print(quoting)
            print('FIM VALIDA TESTE UNITARIO quoting')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO doublequote')
            print(doublequote)
            print('FIM VALIDA TESTE UNITARIO doublequote')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO escapechar')
            print(escapechar)
            print('FIM VALIDA TESTE UNITARIO escapechar')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO comment')
            print(comment)
            print('FIM VALIDA TESTE UNITARIO comment')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO encoding')
            print(encoding)
            print('FIM VALIDA TESTE UNITARIO encoding')
            print('###############################')

            print('###############################')
            print('VALIDA TESTE UNITARIO storage_options')
            print(storage_options)
            print('FIM VALIDA TESTE UNITARIO storage_options')
            print('###############################')

            data = {
                'sep':sep,
                'delimiter':delimiter,
                
                'skipinitialspace':skipinitialspace,
                'nrows':nrows,
                'keep_default_na':keep_default_na,
                'verbose':verbose,
                'skip_blank_lines':skip_blank_lines,
                'infer_datetime_format':infer_datetime_format,
                'keep_date_col':keep_date_col,
                'cache_dates':cache_dates,
                'iterator':iterator,
                'thousands':thousands,
                'decimal':decimal,
                'lineterminator':lineterminator,
                'quoting':quoting,
                'doublequote':doublequote,
                'escapechar':escapechar,
                'comment':comment,
                'encoding':encoding,
                'storage_options':storage_options

            }
            with open('csv_tojson.json',"w") as arq_json:
                arq_json.write("")
                arq_json.close()

                r = pd.read_csv("media/csv/" + file_name, sep=sep, delimiter=delimiter,                                           
                                skipinitialspace=skipinitialspace,nrows=nrows,
                                keep_default_na=keep_default_na,verbose=verbose,skip_blank_lines=skip_blank_lines,
                                infer_datetime_format=infer_datetime_format,keep_date_col=keep_date_col,
                                cache_dates=cache_dates,iterator=iterator,
                                thousands=thousands,decimal=decimal,lineterminator=lineterminator,quoting=quoting,doublequote=doublequote,
                                escapechar=escapechar,comment=comment,encoding=encoding,
                                storage_options=storage_options)  

                f = r.to_json('csv_tojson.json', indent=1, orient='records')

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
                    
    @action(detail=True, methods=['GET'])
    def my_post(self,request,pk=None):
        
        queryset = Csv_Model.objects.latest('id')
        with open('csv_tojson.json') as m_json:
            dados = json.load(m_json)
            
            return Response(dados)
        return Response({'msg':'blank'})
    
    @action(detail=True, methods=['GET'])
    def comunicator(self,request, pk=None):
        
        queryset = Csv_Model.objects.latest('id')
        
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
    
                

                
                   
