# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_auto_20160711_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='parent_id',
            new_name='parent',
        ),
        migrations.RenameField(
            model_name='keyschool',
            old_name='org_id',
            new_name='org',
        ),
        migrations.RenameField(
            model_name='org',
            old_name='area_id',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='org',
            old_name='parent_id',
            new_name='parent',
        ),
        migrations.RenameField(
            model_name='userpermissions',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='userrelationinfo',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='userstatuschangelog',
            old_name='use_id',
            new_name='use',
        ),
        migrations.RemoveField(
            model_name='user',
            name='md5passwdstr',
        ),
        migrations.RemoveField(
            model_name='userpermissions',
            name='permission_id',
        ),
        migrations.AddField(
            model_name='userpermissions',
            name='permission',
            field=models.IntegerField(default=0, db_column=b'permission_id'),
        ),
        migrations.AlterField(
            model_name='codeaccounttype',
            name='comments',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='coderole',
            name='comments',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='comments',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='comments',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='userrelationinfo',
            name='comments',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
