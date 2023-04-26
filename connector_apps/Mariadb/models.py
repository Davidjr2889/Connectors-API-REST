from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MariaDb_Model(Base):
    host = models.CharField(max_length=255, blank=False)
    database = models.CharField(max_length=255, blank=False)
    username = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)
    port = models.IntegerField(default=True, blank=False)
    table_mariadb = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f"File id: {self.pk}"