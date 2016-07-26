# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0009_auto_20160724_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.FloatField(verbose_name=b'\xe7\x89\x88\xe6\x9c\xac')),
                ('url', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe5\x9c\xb0\xe5\x9d\x80')),
                ('comments', models.TextField(verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe5\x86\x85\xe5\xae\xb9')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
            options={
                'db_table': 'version',
                'verbose_name': 'APP \u7248\u672c',
                'verbose_name_plural': 'APP \u7248\u672c',
            },
        ),
    ]
