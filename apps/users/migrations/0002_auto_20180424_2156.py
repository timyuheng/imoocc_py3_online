# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-24 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_level',
            field=models.CharField(choices=[('0', '普通用户'), ('1', '后台管理员'), ('2', '超级管理员')], default='0', max_length=2, verbose_name='用户权限等级'),
        ),
    ]
