# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0041_variation_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='gluten_free_options_upon_request',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variation',
            name='vegetarian_options_upon_request',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
    ]
