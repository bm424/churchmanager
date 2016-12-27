# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churchmanager', '0009_church_map_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='church',
            name='show_map',
            field=models.BooleanField(default=True, help_text='Choose whether or not to display the location of the church as a Google map.'),
        ),
        migrations.AlterField(
            model_name='church',
            name='map_query',
            field=models.CharField(blank=True, editable=False, max_length=200),
        ),
    ]
