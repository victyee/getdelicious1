# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20150504_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='message',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='subject',
        ),
    ]
