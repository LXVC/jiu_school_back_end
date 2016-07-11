# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20160710_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='parent_id',
            field=models.ForeignKey(db_column=b'parent_id', blank=True, to='education.Org', null=True),
        ),
    ]
