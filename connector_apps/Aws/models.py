from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        
        
class Aws_Model(Base):
    
    aw_access_key = models.CharField(max_length=80)
    aws_secret_access = models.CharField(max_length=100)
    bucket_name = models.CharField(max_length=80)
    bucket_prefix = models.CharField(max_length=80)