# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admission', '0002_auto_20151025_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='receiveremail',
            field=models.CharField(default=1, max_length=500),
        ),
        migrations.AddField(
            model_name='chat',
            name='senderemail',
            field=models.CharField(default=1, max_length=500),
        ),
    ]
