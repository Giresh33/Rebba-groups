# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-25 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_auto_20181016_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultation',
            old_name='doctor_name',
            new_name='doctor',
        ),
    ]
