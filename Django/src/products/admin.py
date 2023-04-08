from django.contrib import admin

# Register your models here.
#Relative import
from .models import Product

admin.site.register(Product)
