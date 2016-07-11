# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_auto_20160711_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='parent_id',
            field=models.ForeignKey(db_column=b'parent_id', blank=True, to='education.Area', null=True),
        ),
    ]
