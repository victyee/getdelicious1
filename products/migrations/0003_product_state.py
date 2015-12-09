# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150429_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='state',
            field=models.CharField(blank=True, max_length=120, null=True, choices=[(b'ACT', b'Australian Capital Territory'), (b'NSW', b'New South Wales'), (b'NT', b'Northern Territory'), (b'QLD', b'Queensland'), (b'SA', b'South Australia'), (b'TAS', b'Tasmania'), (b'VIC', b'Victoria'), (b'WA', b'Western Australia')]),
            preserve_default=True,
        ),
    ]
