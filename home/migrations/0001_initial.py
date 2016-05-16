# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='IconFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('icon', models.ImageField(upload_to='icons_files/')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, max_length=250)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('contenu', models.TextField(null=True)),
                ('date_realisation', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('categories', models.ManyToManyField(to='home.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('version', models.CharField(max_length=30)),
                ('fichier', models.FileField(upload_to='resources/')),
                ('project', models.ForeignKey(to='home.Project')),
                ('type', models.ForeignKey(to='home.IconFile')),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('icon', models.ImageField(upload_to='icons_tools/')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tools',
            field=models.ManyToManyField(to='home.Tool'),
        ),
        migrations.AddField(
            model_name='image',
            name='project',
            field=models.ForeignKey(to='home.Project'),
        ),
    ]
