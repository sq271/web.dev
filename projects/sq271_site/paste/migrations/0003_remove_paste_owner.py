# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0002_paste_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paste',
            name='owner',
        ),
    ]
