# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-12 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_v330_delete_authtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='unifiedjob',
            name='emitted_events',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
