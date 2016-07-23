# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_notice_noticeto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeaccounttype',
            name='acc_type_name',
            field=models.CharField(default=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7', max_length=20),
        ),
        migrations.AlterField(
            model_name='codeeduperiod',
            name='edu_period_name',
            field=models.CharField(default=b'\xe4\xb8\xad\xe5\xad\xa6', max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='codeuserstatus',
            name='user_state_name',
            field=models.CharField(default=b'\xe5\x9c\xa8\xe7\xba\xbf', max_length=20),
        ),
    ]
