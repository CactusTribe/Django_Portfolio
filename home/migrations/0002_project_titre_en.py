# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='titre_en',
            field=models.CharField(max_length=100, null=True),
        ),
    ]