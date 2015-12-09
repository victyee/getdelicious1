# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_auto_20150504_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(default=b'package', max_length=120, choices=[(b'package', b'package')]),
            preserve_default=True,
        ),
    ]
