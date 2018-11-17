from __future__ import unicode_literals
from django.db import models
from django.contrib import admin


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

@admin.register(Property)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['description', 'price', 'city', 'photo']
    ordering = ('description',)
    actions = None

