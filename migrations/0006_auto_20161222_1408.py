# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 14:08
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('churchmanager', '0005_church_classification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='church',
            name='list_crop',
            field=image_cropping.fields.ImageRatioField('photo', '360x240', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='list crop'),
        ),
    ]
