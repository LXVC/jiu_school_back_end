# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeAccountType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('acc_type_name', models.CharField(max_length=20)),
                ('comments', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'code_account_type',
            },
        ),
        migrations.CreateModel(
            name='CodeRole',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('role_name', models.CharField(max_length=20)),
                ('comments', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'code_role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('account_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('permission_id', models.IntegerField()),
                ('user_id', models.ForeignKey(verbose_name=b'user_id', to='education.User')),
            ],
            options={
                'db_table': 'user_permissions',
            },
        ),
    ]
