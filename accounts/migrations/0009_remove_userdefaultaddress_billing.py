# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20150503_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdefaultaddress',
            name='billing',
        ),
    ]
