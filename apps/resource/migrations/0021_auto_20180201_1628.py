# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-01 16:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0020_auto_20180201_1625'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='YearBooksCover',
            new_name='YearBooksDes',
        ),
    ]
