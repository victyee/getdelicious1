# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0038_auto_20150506_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='about_us',
            field=models.TextField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='contact_number',
            field=models.CharField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='slogan',
            field=models.TextField(max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([]),
        ),
    ]
