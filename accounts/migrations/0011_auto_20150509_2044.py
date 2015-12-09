# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_useraddress_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='truckownerstatus',
            old_name='foodtruck',
            new_name='foodtruck_owner',
        ),
    ]
