# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20150504_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='contact_number',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='message',
            field=models.TextField(default=1, max_length=850),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='subject',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
