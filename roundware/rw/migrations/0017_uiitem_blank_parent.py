# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-18 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rw', '0016_tags_uigroups_api2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uiitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rw.UIItem'),
        ),
    ]