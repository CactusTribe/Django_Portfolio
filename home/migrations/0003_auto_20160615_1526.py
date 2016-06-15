# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_project_titre_en'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='titre_en',
            new_name='titre_traduction',
        ),
        migrations.AddField(
            model_name='categorie',
            name='nom_traduction',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='description_traduction',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='contenu_traduction',
            field=models.TextField(null=True),
        ),
    ]