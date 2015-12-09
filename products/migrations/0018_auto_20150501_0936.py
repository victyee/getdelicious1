# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20150501_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='image',
            field=models.ImageField(default=1, upload_to=b'foodtruck/packages/'),
            preserve_default=False,
        ),
    ]
