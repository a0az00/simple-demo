# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20171119_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsprofile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='goods/goods_profile/images', verbose_name='展示图'),
        ),
    ]