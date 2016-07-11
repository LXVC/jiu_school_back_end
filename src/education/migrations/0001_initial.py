# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('path', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=50)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('level', models.SmallIntegerField()),
                ('sort', models.IntegerField()),
                ('status', models.SmallIntegerField()),
                ('parent_id', models.ForeignKey(db_column=b'parent_id', blank=True, to='education.Area', null=True)),
            ],
            options={
                'db_table': 'area',
            },
        ),
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
            name='CodeEduPeriod',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('edu_period_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'code_edu_period',
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
            name='CodeUserStatus',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('user_state_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'code_user_status',
            },
        ),
        migrations.CreateModel(
            name='KeySchool',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('type', models.IntegerField()),
            ],
            options={
                'db_table': 'keyschool',
            },
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('path', models.CharField(max_length=200)),
                ('level', models.SmallIntegerField()),
                ('sort', models.IntegerField()),
                ('status', models.SmallIntegerField()),
                ('created_date', models.DateTimeField()),
                ('comments', models.CharField(max_length=500)),
                ('area_id', models.ForeignKey(to='education.Area', db_column=b'area_id')),
                ('edu_period', models.ForeignKey(to='education.CodeEduPeriod', db_column=b'edu_period')),
                ('parent_id', models.ForeignKey(db_column=b'parent_id', blank=True, to='education.Org', null=True)),
            ],
            options={
                'db_table': 'org',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('account_id', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('login_name', models.CharField(max_length=50)),
                ('md5passwdstr', models.CharField(max_length=300)),
                ('gender', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
                ('idcardnum', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('intro', models.CharField(max_length=500)),
                ('qq', models.CharField(max_length=20)),
                ('wechat', models.CharField(max_length=100)),
                ('inschoolyears', models.IntegerField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_login_date', models.DateTimeField()),
                ('last_status_change_date', models.DateTimeField()),
                ('permissgroucp', models.IntegerField()),
                ('head_pic_url', models.CharField(max_length=1000)),
                ('comments', models.CharField(max_length=500)),
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
            ],
            options={
                'db_table': 'user_permissions',
            },
        ),
        migrations.CreateModel(
            name='UserStatusChangeLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('change_date', models.DateTimeField()),
                ('resason', models.CharField(max_length=500)),
                ('new_status', models.ForeignKey(related_name='new_status', db_column=b'new_status', to='education.CodeUserStatus')),
                ('old_status', models.ForeignKey(related_name='old_status', db_column=b'old_status', to='education.CodeUserStatus')),
            ],
            options={
                'db_table': 'user_status_change_log',
            },
        ),
        migrations.CreateModel(
            name='UserRelationInfo',
            fields=[
                ('user_id', models.OneToOneField(primary_key=True, db_column=b'user_id', serialize=False, to='education.User')),
                ('relation_type', models.CharField(max_length=10)),
                ('relation_name', models.CharField(max_length=50)),
                ('relation_phone', models.CharField(max_length=32)),
                ('relation_email', models.EmailField(max_length=254)),
                ('relation_address', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'user_relation_info',
            },
        ),
        migrations.AddField(
            model_name='userstatuschangelog',
            name='oper',
            field=models.ForeignKey(related_name='operator', db_column=b'oper', to='education.User'),
        ),
        migrations.AddField(
            model_name='userstatuschangelog',
            name='use_id',
            field=models.ForeignKey(related_name='who', db_column=b'user_id', to='education.User'),
        ),
        migrations.AddField(
            model_name='userpermissions',
            name='user_id',
            field=models.ForeignKey(to='education.User', db_column=b'user_id'),
        ),
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.ForeignKey(to='education.CodeAccountType', db_column=b'account_type'),
        ),
        migrations.AddField(
            model_name='user',
            name='org_id',
            field=models.ForeignKey(to='education.Org', db_column=b'org_id'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(to='education.CodeRole', db_column=b'role'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.ForeignKey(to='education.CodeUserStatus', db_column=b'status'),
        ),
        migrations.AddField(
            model_name='keyschool',
            name='org_id',
            field=models.ForeignKey(to='education.Org', db_column=b'org_id'),
        ),
    ]
