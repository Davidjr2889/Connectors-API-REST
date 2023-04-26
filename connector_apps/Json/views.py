from rest_framework import viewsets,status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Json_Model
from .serializers import Json_Serializer

import pandas as pd
import json



class JsonViewSet(viewsets.ModelViewSet):
    queryset = Json_Model.objects.all()
    
    def get_queryset(self):
        queryset = Json_Model.objects.all()
        return queryset
    
    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset, pk=pk)
        return obj
    
    def get_serializer_class(self):
        return Json_Serializer
    
    def perform_create(self, serializer):
        serializer.save()
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        file = request.FILES['file']
        file_name = str(file)
        
        if file_name.endswith('.json'):
            self.perform_create(serializer)
            
            
            orient = serializer.data['orient']
            typ = serializer.data['typ']
            dtype = serializer.data['dtype']
            convert_axes = serializer.data['convert_axes']
            convert_dates = serializer.data['convert_dates'] 
            keep_default_dates = serializer.data['keep_default_dates']
            numpy = serializer.data['numpy']
            precise_float = serializer.data['precise_float']
            date_unit = serializer.data['date_unit']
            encoding = serializer.data['encoding']
            encoding_errors = serializer.data['encoding_errors']
            lines = serializer.data['lines']
            chunksize = serializer.data['chunksize']
            compression = serializer.data['compression']
            nrows = serializer.data['nrows']
            storage_options = serializer.data['storage_options']
            
            if serializer.data['orient'] == '':
                orient = None
            if serializer.data['typ'] == '':
                typ = 'frame'
            if serializer.data['dtype'] == '':
                dtype = None
            if serializer.data['convert_axes'] == '':
                convert_axes = None
            if serializer.data['convert_dates'] == '':
                convert_dates = True
            if serializer.data['keep_default_dates'] == '':
                keep_default_dates = True
            if serializer.data['numpy'] == '':
                numpy = False
            if serializer.data['precise_float'] == '':
                precise_float = False
            if serializer.data['date_unit'] == '':
                date_unit = None
            if serializer.data['encoding'] == '':
                encoding = None
            if serializer.data['encoding_errors'] == '':
                encoding_errors = 'strict'
            if serializer.data['lines'] == '':
                lines = False
            if serializer.data['chunksize'] == '':
                chunksize = None
            if serializer.data['compression'] == '':
                compression = 'infer'
            if serializer.data['nrows'] == '':
                nrows = None
            if serializer.data['storage_options'] == '':
                storage_options = None
            with open('json_tojson.json','w') as m_json:
                m_json.write("")
                m_json.close()
                
                df = pd.read_json('media/json/' + file_name ,orient=orient, typ=typ,
                                dtype=dtype, convert_axes=convert_axes, convert_dates=convert_dates, 
                                keep_default_dates=keep_default_dates, numpy=numpy, 
                                precise_float=precise_float, date_unit=date_unit, encoding=encoding, 
                                encoding_errors=encoding_errors, lines=lines, chunksize=chunksize, 
                                compression=compression, nrows=nrows, storage_options=storage_options)
                
                f = df.to_json('csv_tojson.json', indent=1, orient='records')
                print(df)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(detail=True, methods=['GET'])
    def my_post(self,request, pk=None):
        with open('json_tojson.json') as m_json:
            dados = json.load(m_json)
            
            return Response(dados, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['GET'])
    def comunicator(self,request, pk=None):
        
        queryset = Json_Model.objects.latest('id')
        
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
    