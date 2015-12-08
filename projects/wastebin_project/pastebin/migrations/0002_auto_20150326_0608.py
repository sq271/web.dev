# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paste',
            name='id',
        ),
        migrations.AddField(
            model_name='paste',
            name='hash',
            field=models.CharField(primary_key=True, unique=True, default=datetime.datetime(2015, 3, 26, 6, 8, 0, 156191, tzinfo=utc), serialize=False, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paste',
            name='private',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='paste',
            name='title',
            field=models.CharField(default='Untitled', max_length=64),
            preserve_default=True,
        ),
    ]
