# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-20 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0004_auto_20170620_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='school',
            field=models.CharField(choices=[('', '---Please select a school---'), ('University of Maryland', 'University of Maryland'), ('Ohio State University', 'Ohio State University'), ('University of Indiana', 'University of Indiana')], max_length=200),
        ),
    ]
