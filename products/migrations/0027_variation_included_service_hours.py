# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20150502_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='included_service_hours',
            field=models.CharField(default=2, max_length=120),
            preserve_default=False,
        ),
    ]
