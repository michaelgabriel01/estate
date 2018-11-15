from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='photos')

class HouseModel(models.Model):
    house_name = models.CharField(max_length=100)
    house_city = models.CharField(max_length=100)
    house_neighborhood = models.CharField(max_length=100)
    house_photo = models.ImageField(storage=fs, default = 'fs/None/pic1.jpg')
    house_id = models.DecimalField(max_length=100, max_digits=10, decimal_places=2)


@admin.register(HouseModel)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['house_name', 'house_city', 'house_neighborhood', 'house_id']
    ordering = ('-house_name',)
    actions = None


class Property(models.Model):
    description = models.CharField(max_length=255, blank=True)
    property_id = models.DecimalField(max_length=100, max_digits=10, decimal_places=2)
    price = models.CharField(max_length=255, blank=True)
    photo = models.FileField(upload_to='documents/')
    date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
