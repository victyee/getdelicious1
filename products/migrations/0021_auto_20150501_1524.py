# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20150501_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='foodtruck_name',
            field=models.CharField(default=b' ', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='owner_name',
            field=models.CharField(max_length=120),
            preserve_default=True,
        ),
    ]
