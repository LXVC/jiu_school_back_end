# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpermissions',
            old_name='user_id',
            new_name='user',
        ),
    ]
