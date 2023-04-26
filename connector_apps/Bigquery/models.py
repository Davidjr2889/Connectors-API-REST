from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        abstract = True

class BigQueryModel(Base):
    file = models.FileField(upload_to='BigQuery/', blank=False)
    dataset = models.CharField(max_length=40, blank=False)
    table = models.CharField(max_length=40, blank=False)
    where = models.CharField(max_length=40, blank=True)