# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrelationinfo',
            name='user_id',
            field=models.OneToOneField(primary_key=True, db_column=b'user_id', serialize=False, to='education.User'),
        ),
    ]
