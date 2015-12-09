# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='price',
            new_name='maximum_guests',
        ),
        migrations.AddField(
            model_name='variation',
            name='mininum_guests',
            field=models.DecimalField(null=True, max_digits=100, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='variation',
            name='price_per_guest',
            field=models.DecimalField(null=True, max_digits=100, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(default=b'package', max_length=120, choices=[(b'package', b'package'), (b'color', b'color')]),
            preserve_default=True,
        ),
    ]
