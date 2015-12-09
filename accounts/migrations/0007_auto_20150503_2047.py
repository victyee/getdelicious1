# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20150503_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='time_from',
            field=models.TextField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddress',
            name='time_to',
            field=models.TextField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='date',
            field=models.TextField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
