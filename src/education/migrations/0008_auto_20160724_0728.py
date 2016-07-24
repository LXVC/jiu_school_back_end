# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0007_auto_20160724_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeaccounttype',
            name='acc_type_name',
            field=models.CharField(default='\u624b\u673a\u53f7', max_length=20),
        ),
        migrations.AlterField(
            model_name='coderole',
            name='role_name',
            field=models.CharField(default='\u5b66\u751f', max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='codeuserstatus',
            name='user_state_name',
            field=models.CharField(default='\u5728\u7ebf', max_length=20),
        ),
    ]
