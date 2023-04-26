from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Postgres_Model(models.Model):
    host = models.CharField(max_length=255)
    database = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    port = models.IntegerField(default=True)
    table_postgres = models.CharField(max_length=50)

    def __str__(self):
        return f"File id: {self.pk}"