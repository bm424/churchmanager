# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churchmanager', '0015_auto_20170105_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='publish',
            field=models.BooleanField(default=False, help_text='Select when the article is ready for publication.'),
        ),
    ]
