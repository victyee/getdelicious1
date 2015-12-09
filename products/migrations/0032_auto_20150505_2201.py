# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_auto_20150505_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='included_service_hours',
            field=models.DecimalField(default=1, max_digits=1000, decimal_places=2),
            preserve_default=False,
        ),
    ]
