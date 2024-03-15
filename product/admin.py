from django.contrib import admin
from .models import Category,Product,Order,OrderItem

# Register your models here.

admin.site.register([Category,Product,Order,OrderItem])



