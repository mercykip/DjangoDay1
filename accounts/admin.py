from django.contrib import admin

# Register your models here.
#relative import
from .models import Account
admin.site.register(Account)
