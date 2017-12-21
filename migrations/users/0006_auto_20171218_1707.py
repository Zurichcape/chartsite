# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20171218_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='work_unit',
            new_name='work',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='unit',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='单位名称'),
        ),
    ]
