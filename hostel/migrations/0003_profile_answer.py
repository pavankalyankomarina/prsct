# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-21 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='answer',
            field=models.BooleanField(default=False),
        ),
    ]
