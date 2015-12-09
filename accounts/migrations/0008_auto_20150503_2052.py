# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20150503_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='contact_person_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddress',
            name='email',
            field=models.EmailField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddress',
            name='message',
            field=models.TextField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='date',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='time_from',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='time_to',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
