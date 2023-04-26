from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class MongoDB_Model(Base):

    hostname = models.CharField(max_length=20, blank=False)
    username = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=20, blank=False)
    cluster_address = models.CharField(max_length=70, blank=False)
    data_base = models.CharField(max_length=20, blank=False)
    table_mongo = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f"Conexão id: {self.pk}"