# Generated by Django 2.0.7 on 2018-11-15 22:03

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(default='fs/None/no-img.jpg', upload_to='fs/')),
            ],
        ),
        migrations.CreateModel(
            name='HouseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(max_length=100)),
                ('house_city', models.CharField(max_length=100)),
                ('house_neighborhood', models.CharField(max_length=100)),
                ('house_photo', models.ImageField(default='fs/None/pic1.jpg', storage=django.core.files.storage.FileSystemStorage(location='photos'), upload_to='')),
                ('house_id', models.DecimalField(decimal_places=2, max_digits=10, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('property_id', models.DecimalField(decimal_places=2, max_digits=10, max_length=100)),
                ('price', models.CharField(blank=True, max_length=255)),
                ('photo', models.FileField(upload_to='documents/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
    ]
