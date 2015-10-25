# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(max_length=500)),
                ('receiver', models.CharField(max_length=500)),
                ('message', models.CharField(max_length=100000)),
                ('senderemail', models.CharField(max_length=500)),
                ('receiveremail', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Enrollment', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('contact', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=18)),
                ('avatar', models.ImageField(upload_to=b'static/Admission/profiles/', null=True, verbose_name=b'profile picture', blank=True)),
            ],
        ),
    ]
