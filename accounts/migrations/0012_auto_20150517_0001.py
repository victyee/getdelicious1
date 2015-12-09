# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20150509_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='state',
            field=models.CharField(default=1, max_length=120, choices=[(b'ACT', b'Australian Capital Territory'), (b'NSW', b'New South Wales'), (b'NT', b'Northern Territory'), (b'QLD', b'Queensland'), (b'SA', b'South Australia'), (b'TAS', b'Tasmania'), (b'VIC', b'Victoria'), (b'WA', b'Western Australia')]),
            preserve_default=False,
        ),
    ]
