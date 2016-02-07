# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paste',
            name='body',
            field=models.TextField(default=datetime.datetime(2016, 1, 8, 0, 55, 28, 565257, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
