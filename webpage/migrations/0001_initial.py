# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=20)),
                ('about', models.CharField(max_length=200)),
                ('images', models.ImageField(height_field=40, upload_to='/webpage/static/webpage/images', width_field=40)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('nick_name', models.CharField(max_length=20)),
                ('image', models.ImageField(height_field=40, upload_to='/webpage/static/webpage/images', width_field=40)),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.User'),
        ),
    ]