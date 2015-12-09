# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availability_link',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
