# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 11:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GoodsImage',
            new_name='ChartImage',
        ),
        migrations.RenameModel(
            old_name='HotSearchWords',
            new_name='HotSearch',
        ),
    ]
