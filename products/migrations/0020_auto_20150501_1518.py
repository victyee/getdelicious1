# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_variation_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='owner_name',
            field=models.CharField(default=b'yea', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variation',
            name='menu',
            field=models.TextField(max_length=50000),
            preserve_default=True,
        ),
    ]
