# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20150430_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'foodtruck/logo/', blank=True),
            preserve_default=True,
        ),
    ]
