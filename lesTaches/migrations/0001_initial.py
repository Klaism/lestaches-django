# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('closed', models.Field(default=False)),
            ],
        ),
    ]