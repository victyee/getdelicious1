# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20150502_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='mininum_guests',
            new_name='minimum_guests',
        ),
    ]
