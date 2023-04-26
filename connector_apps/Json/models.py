from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Json_Model(Base):
    file = models.FileField(upload_to='json/', blank=False)
    orient = models.CharField(max_length=40, blank=True)
    typ = models.CharField(max_length=40, blank=True)
    dtype = models.CharField(max_length=40, blank=True)
    convert_axes = models.CharField(max_length=40, blank=True)
    convert_dates = models.CharField(max_length=40, blank=True) 
    keep_default_dates = models.CharField(max_length=40, blank=True)
    numpy = models.CharField(max_length=40, blank=True)
    precise_float = models.CharField(max_length=40, blank=True)
    date_unit = models.CharField(max_length=40, blank=True)
    encoding = models.CharField(max_length=40, blank=True)
    encoding_errors = models.CharField(max_length=40, blank=True)
    lines = models.CharField(max_length=40, blank=True)
    chunksize = models.CharField(max_length=40, blank=True)
    compression = models.CharField(max_length=40, blank=True)
    nrows = models.CharField(max_length=40, blank=True)
    storage_options = models.CharField(max_length=40, blank=True)