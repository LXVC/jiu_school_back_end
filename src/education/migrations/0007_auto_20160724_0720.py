# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_auto_20160723_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='latitude',
            field=models.FloatField(default=2.2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='longitude',
            field=models.FloatField(default=1.1, null=True, blank=True),
        ),
    ]
