# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0040_remove_variation_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
