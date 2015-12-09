# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_auto_20150504_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='contact_number',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=120, choices=[(b'BE', b'Bookings Enquiry'), (b'GE', b'General Enquiry'), (b'YGR', b'You guys rock!!'), (b'ME', b'Media Enquiry'), (b'FTO', b"I'm a foodtruck owner and would like more info"), (b'CO', b'Complaints'), (b'SU', b'Suggestions'), (b'OT', b'Others')]),
            preserve_default=True,
        ),
    ]
