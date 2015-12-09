# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150430_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='zipcode',
            new_name='postcode',
        ),
        migrations.AddField(
            model_name='useraddress',
            name='date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
