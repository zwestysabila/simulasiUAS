from django.db import models

# Create your models here.
from django.db import models

class List(models.Model):
    pass

class Item(models.Model):
    angka = models.IntegerField(default=0)
    angkaacak = models.IntegerField(default=0)
    statusnya = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
