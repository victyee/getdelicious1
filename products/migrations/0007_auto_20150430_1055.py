# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150430_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='contact_number',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='owner_name',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
