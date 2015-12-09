# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=120)),
                ('contact_number', models.CharField(max_length=100, null=True, blank=True)),
                ('subject', models.CharField(max_length=120)),
                ('message', models.TextField(max_length=850)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
