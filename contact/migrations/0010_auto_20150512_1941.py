# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_auto_20150505_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='contact_number',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
