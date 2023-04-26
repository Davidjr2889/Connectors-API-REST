from django.db import models

class Base(models.Model):
    updated = models.DateTimeField(auto_now_add=True) 
    created = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Xls_Model(Base):
    file = models.FileField(upload_to='xls/', blank=False)
    sheet_name = models.CharField(max_length=40, blank=True)
    header =  models.CharField(max_length=40, blank=True)
    names = models.CharField(max_length=40, blank=True)
    index_col = models.CharField(max_length=40, blank=True) 
    usecols = models.CharField(max_length=40, blank=True) 
    squeeze = models.CharField(max_length=40, blank=True) 
    dtype = models.CharField(max_length=40, blank=True) 
    engine = models.CharField(max_length=40, blank=True) 
    converters = models.CharField(max_length=40, blank=True) 
    true_values = models.CharField(max_length=40, blank=True) 
    false_values = models.CharField(max_length=40, blank=True) 
    skiprows = models.CharField(max_length=40, blank=True) 
    nrows = models.CharField(max_length=40, blank=True) 
    na_values = models.CharField(max_length=40, blank=True) 
    keep_default_na = models.CharField(max_length=40, blank=True) 
    na_filter = models.CharField(max_length=40, blank=True)
    verbose  = models.CharField(max_length=40, blank=True)
    parse_dates = models.CharField(max_length=40, blank=True)
    date_parser = models.CharField(max_length=40, blank=True) 
    thousands = models.CharField(max_length=40, blank=True) 
    decimal = models.CharField(max_length=40, blank=True)
    comment = models.CharField(max_length=40, blank=True) 
    skipfooter = models.CharField(max_length=40, blank=True) 
    convert_float = models.CharField(max_length=40, blank=True) 
    mangle_dupe_cols = models.CharField(max_length=40, blank=True)
    storage_options = models.CharField(max_length=40, blank=True)
        