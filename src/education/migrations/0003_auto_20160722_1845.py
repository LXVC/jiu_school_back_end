# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20160719_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='org_id',
        ),
        migrations.AddField(
            model_name='org',
            name='type',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='org',
            field=models.ForeignKey(related_name='users', db_column=b'org_id', blank=True, to='education.Org', null=True),
        ),
    ]
