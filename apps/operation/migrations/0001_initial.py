# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 11:21
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('chart', models.ForeignKey(db_column='添加时间', help_text='图片id', on_delete=django.db.models.deletion.CASCADE, to='chart.Chart', verbose_name='图片')),
                ('user', models.ForeignKey(db_column='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name_plural': '用户收藏',
                'verbose_name': '用户收藏',
            },
        ),
        migrations.CreateModel(
            name='UserLeavingMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.IntegerField(choices=[(1, '留言'), (2, '投诉'), (3, '询问'), (4, '售后'), (5, '求购')], db_column='留言类型', default=1, help_text='留言类型: 1(留言),2(投诉),3(询问),4(售后),5(求购)', verbose_name='留言类型')),
                ('subject', models.CharField(db_column='主题', default='', max_length=100, verbose_name='主题')),
                ('message', models.TextField(db_column='留言内容', default='', help_text='留言内容', verbose_name='留言内容')),
                ('file', models.FileField(db_column='上传的文件', help_text='上传的文件', upload_to='message/images/', verbose_name='上传的文件')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('user', models.ForeignKey(db_column='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name_plural': '用户留言',
                'verbose_name': '用户留言',
            },
        ),
        migrations.AlterUniqueTogether(
            name='userfav',
            unique_together=set([('user', 'chart')]),
        ),
    ]
