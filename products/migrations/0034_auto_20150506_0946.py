# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_auto_20150506_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='availability_link',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
    ]
