from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Html_Model

from django.shortcuts import get_object_or_404

from . serializers import Html_Serializer

import pandas as pd
import json


class HtmlViewSet(viewsets.ModelViewSet):
    queryset = Html_Model.objects.all()
    
    
    def get_queryset(self):
        queryset = Html_Model.objects.all()
        return queryset
        
    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset,pk=pk)
        return obj
        
    def get_serializer_class(self):
        return Html_Serializer
    
    def perform_create(self, serializer):
        serializer.save()
    
    
    def create(self, request, *args, **kwargs):
        
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    
        self.perform_create(serializer)
        
        url = serializer.data['url']
        url_str = str(url)
        flavor = serializer.data['flavor']
        header = serializer.data['header']
        index_col = serializer.data['index_col'] 
        skiprows = serializer.data['skiprows']
        attrs = serializer.data['attrs']
        parse_dates = serializer.data['parse_dates']
        thousands = serializer.data['thousands']
        encoding = serializer.data['encoding']
        decimal = serializer.data['decimal']
        converters = serializer.data['converters']
        na_values = serializer.data['na_values']
        keep_default_na = serializer.data['keep_default_na']
        displayed_only = serializer.data['displayed_only']
        extract_links = serializer.data['extract_links']
        
        if serializer.data['flavor'] == '':
            flavor = None
        if serializer.data['header'] == '':
            header = None
        if serializer.data['index_col'] == '':
            index_col = None
        if serializer.data['skiprows'] == '':
            skiprows = None
        if serializer.data['attrs'] == '':
            attrs = None
        if serializer.data['parse_dates'] == '':
            parse_dates = False
        if serializer.data['thousands'] == '':
            thousands = ','
        if serializer.data['encoding'] == '':
            encoding = None
        if serializer.data['decimal'] == '':
            decimal = '.'
        if serializer.data['converters'] == '':
            converters = None
        if serializer.data['na_values'] == '':
            na_values = None
        if serializer.data['keep_default_na'] == '':
            keep_default_na = True
        if serializer.data['displayed_only'] == '':
            displayed_only = True
        if serializer.data['extract_links'] == '':
            extract_links = None

        if url_str.endswith('.html'):                                               
        
            with open('html_tojson.json','w') as d_json:
                d_json.write("")
                d_json.close()
                
                df = pd.read_html(io=url,flavor=flavor, header=header, index_col=index_col, 
                                    skiprows=skiprows, attrs=attrs, parse_dates=parse_dates,
                                    thousands=thousands, encoding=encoding, decimal=decimal, 
                                    converters=converters, na_values=na_values, 
                                    keep_default_na=keep_default_na, 
                                    displayed_only=displayed_only, extract_links=extract_links)
                
                f = df.to_json('html_tojson.json', indent=1, orient='records')
                
                
                    
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['GET'])
    def my_post(self,request,pk=None):
        with open('html_tojson.json') as d_json:
            dados = json.load(d_json)
        return Response(dados)
    
    @action(detail=True, methods=['GET'])
    def comunicator(self,request, pk=None):
        
        queryset = Html_Model.objects.latest('id')
        
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