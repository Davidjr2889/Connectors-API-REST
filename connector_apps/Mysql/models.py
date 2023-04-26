from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class MySql_Model(Base):
    host = models.CharField(max_length=70, blank=False)
    username = models.CharField(max_length=70, blank=False)
    password = models.CharField(max_length=70, blank=False)
    database = models.CharField(max_length=70, blank=False)
    table_mysql = models.CharField(max_length=70, blank=False)

    def __str__(self):
        return f"DataBase id: {self.pk}"