# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0004_userprofile_should_get_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='is_receiving_agency',
            field=models.BooleanField(default=False),
        ),
    ]
