# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-07 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcode',
            name='email',
            field=models.CharField(max_length=20, verbose_name='邮箱'),
        ),
    ]