# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-28 22:09
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0005_auto_20180118_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcelist',
            name='desc',
            field=DjangoUeditor.models.UEditorField(db_column='数据描述', default='', verbose_name='数据描述'),
        ),
        migrations.AlterField(
            model_name='zgzynywhyc',
            name='content',
            field=DjangoUeditor.models.UEditorField(db_column='内容', default='', verbose_name='内容'),
        ),
    ]