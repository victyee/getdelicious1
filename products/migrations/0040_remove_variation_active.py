# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_auto_20150511_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='active',
        ),
    ]
