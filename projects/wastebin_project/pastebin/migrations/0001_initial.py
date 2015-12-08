# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.TextField()),
                ('owner', models.CharField(blank=True, max_length=32)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-time',),
            },
            bases=(models.Model,),
        ),
    ]
