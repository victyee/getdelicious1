# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_auto_20150506_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='image',
        ),
    ]
