# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_auto_20150506_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='gluten_free_options_upon_request',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='variation',
            name='vegetarian_options_upon_request',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
