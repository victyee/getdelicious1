# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_userdefaultaddress_billing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='country',
        ),
    ]
