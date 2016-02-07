# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('hash', models.CharField(primary_key=True, unique=True, serialize=False, max_length=64)),
                ('title', models.CharField(default='Untitled', max_length=64)),
                ('owner', models.CharField(max_length=32, blank=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('private', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-time',),
            },
        ),
    ]
