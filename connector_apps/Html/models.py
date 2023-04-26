from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    
    class Meta:
        abstract = True
        
class Html_Model(Base):
    url = models.CharField(max_length=100, blank=False)
    flavor = models.CharField(max_length=40, blank=True)
    header = models.CharField(max_length=40, blank=True)
    index_col = models.CharField(max_length=40, blank=True) 
    skiprows = models.CharField(max_length=40, blank=True)
    attrs = models.CharField(max_length=40, blank=True)
    parse_dates = models.CharField(max_length=40, blank=True)
    thousands = models.CharField(max_length=40, blank=True)
    encoding = models.CharField(max_length=40, blank=True)
    decimal = models.CharField(max_length=40, blank=True)
    converters = models.CharField(max_length=40, blank=True)
    na_values = models.CharField(max_length=40, blank=True)
    keep_default_na = models.CharField(max_length=40, blank=True)
    displayed_only = models.CharField(max_length=40, blank=True)
    extract_links = models.CharField(max_length=40, blank=True)
    
    
    
    