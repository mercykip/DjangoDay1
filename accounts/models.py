from django.db import models

# Create your models here.
class Account(models.Model):
    title           =   models.CharField(max_length=120)#max_length=required
    description     =   models.TextField(blank=True,null=True)
    amount          =   models.FloatField()
    summary         =   models.TextField(default='this is cool')
    maritalstatatus =   models.BooleanField(null=True)
