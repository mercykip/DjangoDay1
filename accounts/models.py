from django.db import models

# Create your models here.
class Account(models.Model):
    title           =   models.TextField()
    description     =   models.TextField()
