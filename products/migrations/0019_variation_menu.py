# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20150501_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='menu',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
