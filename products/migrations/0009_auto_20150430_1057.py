# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20150430_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='state',
            new_name='operating_state',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='about_us',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slogan',
            field=models.TextField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
