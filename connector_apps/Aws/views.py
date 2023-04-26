from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Aws_Model
from .serializers import Aws_Serializer

import boto3
from botocore.exceptions import ClientError
from boto3.session import Session
import os
from django.conf import settings
from django.conf.urls.static import static

import pandas as pd

class AwsViewSet(viewsets.ModelViewSet):
    
    queryset = Aws_Model.objects.all()
    

    def get_queryset(self):
        queryset = Aws_Model.objects.all()
        return queryset
    
    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset, pk=pk)
    
    def get_serializer_class(self):
        return Aws_Serializer
    
    def perform_create(self, serializer):
        serializer.save()
    
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exceptions=True)
        self.perform_create(serializer)
        
        pk = serializer.data['id']
        id_aws = serializer.data['aw_access_key']
        password = serializer.data['aws_secret_access']
        b_name = serializer.data['bucket_name']
        b_prefix = serializer.data['bucket_prefix']

        """
        Connect to S3 Service
        """
        session = Session(
        aws_access_key_id=id_aws,
        aws_secret_access_key=password
        )
        print(session)
        data_file_folder = os.path.join(os.getcwd(),'media/')

        s3 = session.resource('s3')
        my_bucket = s3.Bucket(b_name)

        for s3_files in my_bucket.objects.all():
            print(s3_files.key)
        print("TESTE CONEXÃO")
        
        if b_prefix.endswith('.csv'):
            
            my_bucket.download_file(b_prefix,'aws/' + b_prefix)
            print(my_bucket.download_file(b_prefix,'aws/' + b_prefix))
            
            
        
        if b_prefix.endswith('.xls'):
            
            my_bucket.download_file(b_prefix,'aws/' + b_prefix)
            print(my_bucket.download_file(b_prefix,'aws/' + b_prefix))
        
        if b_prefix.endswith('.xlsx'):
            
            my_bucket.download_file(b_prefix,'aws/' + b_prefix)
            print(my_bucket.download_file(b_prefix,'aws/' + b_prefix))
        
        

        
        return Response('Success')