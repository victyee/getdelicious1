# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20150501_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='foodtruck_name',
            field=models.CharField(default=b' ', max_length=120),
            preserve_default=True,
        ),
    ]
