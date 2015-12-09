# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='hour',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
