# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='foodtruck_name',
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('foodtruck_name', 'slug')]),
        ),
    ]
