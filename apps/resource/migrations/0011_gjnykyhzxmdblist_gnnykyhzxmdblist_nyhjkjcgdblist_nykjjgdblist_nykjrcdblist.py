# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-09 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0010_auto_20180108_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='GjnykyhzxmDbList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='项目名称', max_length=255, verbose_name='项目名称')),
                ('desc', models.TextField(db_column='项目简介', verbose_name='项目简介')),
                ('unit', models.CharField(db_column='承担机构', max_length=255, verbose_name='承担机构')),
                ('keywords', models.CharField(db_column='关键词', max_length=128, verbose_name='关键词')),
                ('advance', models.TextField(db_column='研究进展', verbose_name='研究进展')),
                ('resource', models.CharField(db_column='项目来源', max_length=64, verbose_name='项目来源')),
                ('organization', models.CharField(db_column='资助机构', max_length=128, verbose_name='资助机构')),
                ('member', models.TextField(db_column='项目成员', verbose_name='项目成员')),
                ('period', models.CharField(db_column='起止时间', max_length=32, verbose_name='起止时间')),
                ('category', models.CharField(db_column='专业分类', max_length=255, verbose_name='专业分类')),
            ],
            options={
                'verbose_name_plural': '国际农业科研项目数据库',
                'verbose_name': '国际农业科研项目数据库',
                'db_table': '国际农业科研项目数据库',
            },
        ),
        migrations.CreateModel(
            name='GnnykyhzxmDbList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='项目名称', max_length=255, verbose_name='项目名称')),
                ('desc', models.TextField(db_column='项目简介', verbose_name='项目简介')),
                ('unit', models.CharField(db_column='承担单位', max_length=255, verbose_name='承担单位')),
                ('member', models.CharField(db_column='研究人员', max_length=64, verbose_name='研究人员')),
                ('resource', models.CharField(db_column='项目来源', max_length=128, verbose_name='项目来源')),
                ('category', models.CharField(db_column='项目类型', max_length=64, verbose_name='项目类型')),
                ('fund', models.CharField(db_column='项目经费', max_length=32, verbose_name='项目经费')),
                ('start', models.CharField(db_column='开始时间', max_length=10, verbose_name='开始时间')),
                ('end', models.CharField(db_column='结束时间', max_length=10, verbose_name='结束时间')),
            ],
            options={
                'verbose_name_plural': '国内农业科技项目数据库',
                'verbose_name': '国内农业科技项目数据库',
                'db_table': '国内农业科技项目数据库',
            },
        ),
        migrations.CreateModel(
            name='NyhjkjcgDbList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='成果名称', max_length=255, verbose_name='成果名称')),
                ('realizer', models.TextField(db_column='完成人', verbose_name='完成人')),
                ('unit', models.TextField(db_column='完成单位', verbose_name='完成单位')),
                ('keywords', models.CharField(db_column='关键词', max_length=128, verbose_name='关键词')),
                ('desc', models.TextField(db_column='简要技术说明', verbose_name='简要技术说明')),
                ('catergory', models.CharField(db_column='成果类别', max_length=32, verbose_name='成果类别')),
                ('reference', models.TextField(db_column='推荐单位', verbose_name='推荐单位')),
                ('location', models.CharField(db_column='奖励地区', max_length=32, verbose_name='奖励地区')),
                ('year', models.CharField(db_column='奖励年度', max_length=16, verbose_name='奖励年度')),
                ('name', models.CharField(db_column='奖励名称', max_length=32, verbose_name='奖励名称')),
                ('grade', models.CharField(db_column='奖励等级', max_length=32, verbose_name='奖励等级')),
                ('register', models.CharField(db_column='成果登记时间', max_length=32, verbose_name='成果登记时间')),
                ('setime', models.CharField(db_column='研究起止时间', max_length=32, verbose_name='研究起止时间')),
                ('cgtxxs', models.CharField(db_column='成果体现形式', max_length=16, verbose_name='成果体现形式')),
                ('cgscjd', models.CharField(db_column='成果所处阶段', max_length=16, verbose_name='成果所处阶段')),
                ('cgsx', models.CharField(db_column='成果属性', max_length=16, verbose_name='成果属性')),
                ('cgsp', models.CharField(db_column='成果水平', max_length=16, verbose_name='成果水平')),
                ('yjxs', models.CharField(db_column='研究形式', max_length=16, verbose_name='研究形式')),
                ('ztfl', models.CharField(db_column='中图分类', max_length=32, verbose_name='中图分类')),
                ('ktly', models.CharField(db_column='课题来源', max_length=16, verbose_name='课题来源')),
                ('ktlxmc', models.CharField(db_column='课题立项名称', max_length=128, verbose_name='课题立项名称')),
                ('ktlxbh', models.CharField(db_column='课题立项编号', max_length=32, verbose_name='课题立项编号')),
                ('jftr', models.CharField(db_column='经费实际投入额（万元）', max_length=16, verbose_name='经费实际投入额')),
                ('pjfs', models.CharField(db_column='评价方式', max_length=16, verbose_name='评价方式')),
                ('pjdw', models.CharField(db_column='评价单位', max_length=64, verbose_name='评价单位')),
                ('pjrq', models.CharField(db_column='评价日期', max_length=32, verbose_name='评价日期')),
                ('zscqxs', models.CharField(db_column='知识产权形式', max_length=16, verbose_name='研究形式')),
                ('yyzt', models.CharField(db_column='应用状态', max_length=16, verbose_name='应用状态')),
                ('zrfw', models.CharField(db_column='转让范围', max_length=16, verbose_name='转让范围')),
                ('tgyys', models.CharField(db_column='推广形式', max_length=16, verbose_name='推广形式')),
                ('lxr', models.CharField(db_column='联系人', max_length=32, verbose_name='联系人')),
                ('phone', models.CharField(db_column='联系人电话', max_length=64, verbose_name='联系人电话')),
                ('email', models.CharField(db_column='联系人email', max_length=255, verbose_name='联系人email')),
                ('address', models.CharField(db_column='单位通讯地址', max_length=512, verbose_name='单位通讯地址')),
                ('postcode', models.CharField(db_column='邮政编码', max_length=6, verbose_name='邮政编码')),
                ('unitphone', models.CharField(db_column='单位电话', max_length=64, verbose_name='单位电话')),
                ('unitfax', models.CharField(db_column='单位传真', max_length=64, verbose_name='单位传真')),
                ('unitnet', models.URLField(db_column='单位网址', max_length=128, verbose_name='单位网址')),
                ('cooperator', models.TextField(db_column='合作完成单位', verbose_name='合作完成单位')),
            ],
            options={
                'verbose_name_plural': '农业获奖科技成果数据库',
                'verbose_name': '农业获奖科技成果数据库',
                'db_table': '农业获奖科技成果数据库',
            },
        ),
        migrations.CreateModel(
            name='NykjjgDbList',
            fields=[
                ('id', models.CharField(db_column='机构编号', max_length=64, primary_key=True, serialize=False, verbose_name='机构编号')),
                ('gfmc', models.CharField(db_column='规范名称', max_length=255, verbose_name='规范名称')),
                ('ywmc', models.CharField(db_column='英文名称', max_length=255, verbose_name='英文名称')),
                ('qtmc', models.CharField(db_column='其他名称', max_length=512, verbose_name='其他名称')),
                ('clnf', models.CharField(db_column='成立年份', max_length=32, verbose_name='成立年份')),
                ('jglx', models.CharField(db_column='机构类型', max_length=32, verbose_name='机构类型')),
                ('szdq', models.CharField(db_column='所在地区', max_length=255, verbose_name='所在地区')),
                ('sjdw', models.CharField(db_column='上级单位', max_length=255, verbose_name='上级单位')),
                ('desc', models.TextField(db_column='机构简介', verbose_name='机构简介')),
                ('ywjs', models.TextField(db_column='英文简介', verbose_name='英文简介')),
                ('field', models.CharField(db_column='研究领域', max_length=512, verbose_name='研究领域')),
                ('xkfl', models.CharField(db_column='学科分类', max_length=512, verbose_name='学科分类')),
                ('rcdw', models.TextField(db_column='人才队伍', verbose_name='人才队伍')),
                ('jgsz', models.TextField(db_column='机构设置', verbose_name='机构设置')),
                ('kjpt', models.TextField(db_column='科技平台', verbose_name='科技平台')),
                ('zycg', models.TextField(db_column='主要成果', verbose_name='主要成果')),
                ('zbqk', models.TextField(db_column='主办期刊', verbose_name='主办期刊')),
                ('address', models.CharField(db_column='通讯地址', max_length=255, verbose_name='通讯地址')),
                ('postcode', models.CharField(db_column='邮政编码', max_length=6, verbose_name='邮政编码')),
                ('phone', models.CharField(db_column='联系电话', max_length=255, verbose_name='联系电话')),
                ('email', models.CharField(db_column='电子邮箱', max_length=255, verbose_name='电子邮箱')),
                ('fax', models.CharField(db_column='传真', max_length=64, verbose_name='传真')),
                ('net', models.CharField(db_column='网址', max_length=255, verbose_name='网址')),
            ],
            options={
                'verbose_name_plural': '农业科技机构数据库',
                'verbose_name': '农业科技机构数据库',
                'db_table': '农业科技机构数据库',
            },
        ),
        migrations.CreateModel(
            name='NykjrcDbList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='姓名', max_length=32, verbose_name='姓名')),
                ('gender', models.CharField(db_column='性别', max_length=2, verbose_name='性别')),
                ('birthday', models.CharField(db_column='出生日期', max_length=32, verbose_name='出生日期')),
                ('education', models.CharField(db_column='学历', max_length=32, verbose_name='学历')),
                ('jobtitle', models.CharField(db_column='职称', max_length=32, verbose_name='职称')),
                ('duty', models.CharField(db_column='职务', max_length=256, verbose_name='职务')),
                ('eduback', models.TextField(db_column='教育背景', verbose_name='教育背景')),
                ('direction', models.CharField(db_column='研究方向', max_length=255, verbose_name='研究方向')),
                ('field', models.CharField(db_column='专业领域', max_length=255, verbose_name='专业领域')),
                ('subject', models.CharField(db_column='学科分类', max_length=64, verbose_name='学科分类')),
                ('unit', models.CharField(db_column='工作单位', max_length=255, verbose_name='工作单位')),
                ('desc', models.TextField(db_column='本人简介', verbose_name='本人简介')),
                ('contri', models.TextField(db_column='主要成就', verbose_name='主要成就')),
                ('location', models.CharField(db_column='所在地区', max_length=32, verbose_name='所在地区')),
                ('unit_type', models.CharField(db_column='单位属性', max_length=32, verbose_name='单位属性')),
                ('unitaddress', models.CharField(db_column='单位地址', max_length=255, verbose_name='单位地址')),
                ('postcode', models.CharField(db_column='单位邮编', max_length=6, verbose_name='单位邮编')),
            ],
            options={
                'verbose_name_plural': '农业科技人才数据库',
                'verbose_name': '农业科技人才数据库',
                'db_table': '农业科技人才数据库',
            },
        ),
    ]