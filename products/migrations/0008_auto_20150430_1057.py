# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20150430_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='contact_number',
            field=models.IntegerField(max_length=15),
            preserve_default=True,
        ),
    ]
