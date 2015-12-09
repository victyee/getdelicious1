# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20150504_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(blank=True, max_length=120, null=True, choices=[(1, b'Bookings Enquiry'), (2, b'General Enquiry'), (3, b'You guys rock!!'), (4, b'Media Enquiry'), (5, b"I'm a foodtruck owner. How do I join?"), (6, b'Complaints'), (7, b'Suggestions'), (8, b'Others')]),
            preserve_default=True,
        ),
    ]
