from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import Xlsx_Model
from .serializers import Xlsx_Serializer
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

import pandas as pd
import json


class XlsxViewSet(viewsets.ModelViewSet):
    queryset = Xlsx_Model.objects.all()
    
    
    def get_queryset(self):
        queryset = Xlsx_Model.objects.all()
        return queryset
    def get_object(self):
        queryset=self.get_queryset()
        pk=self.kwargs.get('pk')
        obj = get_object_or_404(queryset,pk=pk)
        
    def get_serializer_class(self):
        return Xlsx_Serializer
    
    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):                     
    
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
            
        
        file = request.FILES['file']
        file_name = str(file)
        if file_name.endswith('.xlsx'):
            
            self.perform_create(serializer)
            print('###############################')
            print('###############################')

            print(serializer.data)
            print('###############################')
            print('###############################')

            sheet_name = serializer.data['sheet_name']
            header = serializer.data['header']
            names = serializer.data['names'] 
            index_col = serializer.data['index_col'] 
            usecols = serializer.data['usecols'] 
            squeeze = serializer.data['squeeze'] 
            dtype = serializer.data['dtype'] 
            engine = serializer.data['engine'] 
            converters = serializer.data['converters'] 
            true_values = serializer.data['true_values'] 
            false_values = serializer.data['false_values']
            skiprows = serializer.data['skiprows'] 
            nrows = serializer.data['nrows'] 
            na_values = serializer.data['na_values'] 
            keep_default_na = serializer.data['keep_default_na'] 
            na_filter = serializer.data['na_filter']
            verbose = serializer.data['verbose'] 
            parse_dates = serializer.data['parse_dates']
            date_parser = serializer.data['date_parser'] 
            thousands = serializer.data['thousands'] 
            decimal = serializer.data['decimal'] 
            comment = serializer.data['comment'] 
            skipfooter = serializer.data['skipfooter'] 
            convert_float = serializer.data['convert_float'] 
            mangle_dupe_cols = serializer.data['mangle_dupe_cols'] 
            storage_options = serializer.data['storage_options']


            
            
            print('###############################')
            if serializer.data['sheet_name'] == '':
                sheet_name = 0
            if serializer.data['header'] == '':
                header = 0
            if serializer.data['names']  == '':
                names = None
            if serializer.data['index_col']  == '':
                index_col = None
            if serializer.data['usecols']  == '':
                usecols = None
            if serializer.data['squeeze']  == '':
                squeeze = None   
            if serializer.data['dtype']  == '':
                dtype = None
            if serializer.data['engine']  == '':
                engine = None  
            if serializer.data['converters']  == '':
                converters = None
            if serializer.data['true_values']  == '':
                true_values = None
            if serializer.data['false_values']  == '':
                false_values = None 
            if serializer.data['skiprows']  == '':
                skiprows = None
            if serializer.data['nrows']  == '':
                nrows = None
            if serializer.data['na_values']  == '':
                na_values = None   
            if serializer.data['keep_default_na']  == '':
                keep_default_na = True
            if serializer.data['na_filter']  == '':
                na_filter = True
            if serializer.data['verbose']  == '':
                verbose = False
            if serializer.data['parse_dates']  == '':
                parse_dates = False
            if serializer.data['date_parser']  == '':
                date_parser = None
            if serializer.data['thousands']  == '':
                thousands = None
            if serializer.data['decimal']  == '':
                decimal = '.'
            if serializer.data['comment']  == '':
                comment = None
            if serializer.data['skipfooter']  == '':
                skipfooter = 0
            if serializer.data['convert_float']  == '':
                convert_float = None
            if serializer.data['mangle_dupe_cols']  == '':
                mangle_dupe_cols = True
            if serializer.data['storage_options']  == '':
                storage_options = None

            #dado = {
            #    'sheet_name': sheet_name,
            #    'header': header,
            #    'names': names
            #}
            

            print('###############################')
            print('VALIDA TESTE UNITARIO storage_options')
            print(storage_options)
            print('FIM VALIDA TESTE UNITARIO storage_options')
            print('###############################')

            
            with open('xlsx_tojson.json',"w") as arq_json:
                arq_json.write("")
                arq_json.close()

                df = pd.read_excel("media/xlsx/" + file_name, sheet_name=sheet_name, header=header, 
                                names=names, index_col=index_col, usecols=usecols, 
                                squeeze=squeeze, dtype=dtype, engine=engine, converters=converters, 
                                true_values=true_values, false_values=false_values, skiprows=skiprows, 
                                nrows=nrows, na_values=na_values, keep_default_na=keep_default_na, 
                                na_filter=na_filter, verbose=verbose, parse_dates=parse_dates, 
                                date_parser=date_parser, thousands=thousands, decimal=decimal, 
                                comment=comment, skipfooter=skipfooter, convert_float=convert_float, 
                                mangle_dupe_cols=mangle_dupe_cols, storage_options=storage_options)
                
                
                f = df.to_json('xlsx_tojson.json', indent=1, orient='records')

                
                
                return Response(serializer.data)
                
            return Response({'MsgError':'Not Content or File Format Wrong'})
        
    @action(detail=True, methods=['GET'])
    def my_post(self, request, pk=None):
        with open('xlsx_tojson.json') as m_json:
            dados = json.load(m_json)
        
            return Response(dados)
        
    @action(detail=True, methods=['GET'])
    def comunicator(self,request, pk=None):
        
        queryset = Xlsx_Model.objects.latest('id')
        
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
                    

            