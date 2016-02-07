# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Linkz',
            fields=[
                ('hash', models.CharField(serialize=False, unique=True, primary_key=True, max_length=64)),
                ('title', models.CharField(default='Untitled', max_length=64)),
                ('body', models.TextField()),
                ('owner', models.CharField(blank=True, max_length=32)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('private', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-time',),
            },
        ),
    ]
