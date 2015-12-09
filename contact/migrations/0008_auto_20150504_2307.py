# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_auto_20150504_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='contact_number',
            field=models.CharField(default=1, max_length=100, choices=[(b'BE', b'Bookings Enquiry'), (b'GE', b'General Enquiry'), (b'YGR', b'You guys rock!!'), (b'ME', b'Media Enquiry'), (b'FTO', b"I'm a foodtruck owner. How do I join?"), (b'CO', b'Complaints'), (b'SU', b'Suggestions'), (b'OT', b'Others')]),
            preserve_default=False,
        ),
    ]
