# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='latitude',
            field=models.FloatField(default=2.2, blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='level',
            field=models.SmallIntegerField(default=4, blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='longitude',
            field=models.FloatField(default=1.1, blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='sort',
            field=models.IntegerField(default=1, blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='status',
            field=models.SmallIntegerField(default=2, blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='status',
            field=models.SmallIntegerField(default=0, blank=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='inschoolyears',
            field=models.IntegerField(default=2013, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='permissgroucp',
            field=models.IntegerField(default=2, blank=True),
        ),
    ]
