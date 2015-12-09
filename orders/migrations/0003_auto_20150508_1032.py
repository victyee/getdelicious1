# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_billing_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'Started', max_length=120, choices=[(b'Started', b'Started'), (b'Abandoned', b'Abandoned'), (b'Credit Hold', b'Credit Hold'), (b'Finished', b'Finished')]),
            preserve_default=True,
        ),
    ]
