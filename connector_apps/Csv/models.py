from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        abstract = True

class Csv_Model(Base):
    
    file = models.FileField(upload_to='csv/', blank=False)
    sep = models.CharField(max_length=40, blank=True)
    delimiter = models.CharField(max_length=40, blank=True)
    skipinitialspace = models.CharField(max_length=40, blank=True)
    nrows = models.CharField(max_length=40, blank=True)
    keep_default_na = models.CharField(max_length=40, blank=True)
    verbose = models.CharField(max_length=40, blank=True)
    skip_blank_lines = models.CharField(max_length=40, blank=True)
    infer_datetime_format = models.CharField(max_length=40, blank=True)
    keep_date_col = models.CharField(max_length=40, blank=True)
    cache_dates = models.CharField(max_length=40, blank=True)
    iterator = models.CharField(max_length=40, blank=True)
    thousands = models.CharField(max_length=40, blank=True) 
    decimal = models.CharField(max_length=40, blank=True)
    lineterminator = models.CharField(max_length=40, blank=True)
    quoting = models.CharField(max_length=40, blank=True)
    doublequote = models.CharField(max_length=40, blank=True)
    escapechar = models.CharField(max_length=40, blank=True)
    comment = models.CharField(max_length=40, blank=True)
    encoding = models.CharField(max_length=40, blank=True)
    storage_options = models.CharField(max_length=40, blank=True)
