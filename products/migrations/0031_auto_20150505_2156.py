# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20150505_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='included_service_hours',
            field=models.DecimalField(null=True, max_digits=1000, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
