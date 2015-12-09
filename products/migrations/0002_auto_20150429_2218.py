# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(default=b'size', max_length=120, choices=[(b'package', b'package'), (b'color', b'color')]),
            preserve_default=True,
        ),
    ]
