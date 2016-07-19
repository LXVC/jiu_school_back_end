# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=200, blank=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('short_name', models.CharField(max_length=50, blank=True)),
                ('longitude', models.FloatField(blank=True)),
                ('latitude', models.FloatField(blank=True)),
                ('level', models.SmallIntegerField(default=True, blank=True)),
                ('sort', models.IntegerField(blank=True)),
                ('status', models.SmallIntegerField(blank=True)),
                ('parent', models.ForeignKey(db_column=b'parent_id', blank=True, to='education.Area', null=True)),
            ],
            options={
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='CodeAccountType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acc_type_name', models.CharField(default=b'13788740727', max_length=20, blank=True)),
                ('comments', models.CharField(max_length=500, blank=True)),
            ],
            options={
                'db_table': 'code_account_type',
            },
        ),
        migrations.CreateModel(
            name='CodeEduPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edu_period_name', models.CharField(default=b'\xe5\xb0\x8f\xe5\xad\xa6', max_length=20, blank=True)),
            ],
            options={
                'db_table': 'code_edu_period',
            },
        ),
        migrations.CreateModel(
            name='CodeRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_name', models.CharField(default=b'\xe5\xad\xa6\xe7\x94\x9f', max_length=20, blank=True)),
                ('comments', models.CharField(max_length=500, blank=True)),
            ],
            options={
                'db_table': 'code_role',
            },
        ),
        migrations.CreateModel(
            name='CodeUserStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_state_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'code_user_status',
            },
        ),
        migrations.CreateModel(
            name='KeySchool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=10, blank=True)),
            ],
            options={
                'db_table': 'keyschool',
            },
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'XX\xe4\xb8\xad\xe5\xad\xa6', max_length=50, blank=True)),
                ('size', models.IntegerField(default=1200, blank=True)),
                ('path', models.CharField(default=b'\xe6\xb9\x96\xe5\x8d\x97', max_length=200, blank=True)),
                ('level', models.SmallIntegerField(default=1, blank=True)),
                ('sort', models.IntegerField(default=2, blank=True)),
                ('status', models.SmallIntegerField(default=0, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.CharField(max_length=500, blank=True)),
                ('area', models.ForeignKey(to='education.Area', db_column=b'area_id')),
                ('edu_period', models.ForeignKey(to='education.CodeEduPeriod', db_column=b'edu_period')),
                ('parent', models.ForeignKey(db_column=b'parent_id', blank=True, to='education.Org', null=True)),
            ],
            options={
                'db_table': 'org',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(related_name='profile', primary_key=True, db_column=b'id', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('account_id', models.CharField(max_length=100, blank=True)),
                ('username', models.CharField(max_length=50, blank=True)),
                ('login_name', models.CharField(max_length=50, blank=True)),
                ('md5passwdstr', models.CharField(max_length=300, blank=True)),
                ('gender', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('phone', models.CharField(max_length=30, blank=True)),
                ('birthday', models.DateField(blank=True)),
                ('idcardnum', models.CharField(max_length=30, blank=True)),
                ('address', models.CharField(max_length=200, blank=True)),
                ('intro', models.CharField(max_length=500, blank=True)),
                ('qq', models.CharField(max_length=20, blank=True)),
                ('wechat', models.CharField(max_length=100, blank=True)),
                ('inschoolyears', models.IntegerField(blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_login_date', models.DateTimeField(blank=True)),
                ('last_status_change_date', models.DateTimeField(blank=True)),
                ('permissgroucp', models.IntegerField(blank=0)),
                ('head_pic_url', models.CharField(max_length=1000, blank=True)),
                ('comments', models.CharField(max_length=500, blank=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.ForeignKey(to='auth.Group', db_column=b'group_id')),
            ],
            options={
                'db_table': 'user_group',
            },
        ),
        migrations.CreateModel(
            name='UserOrg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('org', models.ForeignKey(to='education.Org', db_column=b'org_id')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'user_id')),
            ],
            options={
                'db_table': 'user_org',
            },
        ),
        migrations.CreateModel(
            name='UserPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permission', models.ForeignKey(db_column=b'permission_id', default=1, to='auth.Permission')),
            ],
            options={
                'db_table': 'user_permissions',
            },
        ),
        migrations.CreateModel(
            name='UserStatusChangeLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('change_date', models.DateTimeField(blank=True)),
                ('resason', models.CharField(default=b'\xe6\x88\x91\xe5\x96\x9c\xe6\xac\xa2', max_length=500)),
                ('new_status', models.ForeignKey(related_name='new', db_column=b'new_status', to='education.CodeUserStatus')),
                ('old_status', models.ForeignKey(related_name='old', db_column=b'old_status', to='education.CodeUserStatus')),
            ],
            options={
                'db_table': 'user_status_change_log',
            },
        ),
        migrations.CreateModel(
            name='UserRelationInfo',
            fields=[
                ('user', models.OneToOneField(primary_key=True, db_column=b'user_id', serialize=False, to='education.Profile')),
                ('relation_type', models.CharField(default=b'\xe7\x88\xb6\xe4\xba\xb2', max_length=10, blank=True)),
                ('relation_name', models.CharField(default=b'\xe6\x9d\x8e\xe5\xa4\xa9\xe4\xb8\x80', max_length=50, blank=True)),
                ('relation_phone', models.CharField(default=b'13788740727', max_length=32)),
                ('relation_email', models.EmailField(default=b'403381161@qq.com', max_length=254, blank=True)),
                ('relation_address', models.CharField(default=b'\xe6\xb9\x96\xe5\x8d\x97', max_length=200)),
                ('comments', models.CharField(max_length=500, blank=True)),
            ],
            options={
                'db_table': 'user_relation_info',
            },
        ),
        migrations.AddField(
            model_name='userstatuschangelog',
            name='oper',
            field=models.ForeignKey(related_name='operator', db_column=b'oper', to='education.Profile'),
        ),
        migrations.AddField(
            model_name='userstatuschangelog',
            name='user',
            field=models.ForeignKey(related_name='statusChange', db_column=b'user_id', to='education.Profile'),
        ),
        migrations.AddField(
            model_name='userpermissions',
            name='user',
            field=models.ForeignKey(to='education.Profile', db_column=b'user_id'),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='user',
            field=models.ForeignKey(to='education.Profile', db_column=b'user_id'),
        ),
        migrations.AddField(
            model_name='profile',
            name='account_type',
            field=models.ForeignKey(to='education.CodeAccountType', db_column=b'account_type'),
        ),
        migrations.AddField(
            model_name='profile',
            name='org_id',
            field=models.ForeignKey(to='education.Org', db_column=b'org_id'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(to='education.CodeRole', db_column=b'role'),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.ForeignKey(to='education.CodeUserStatus', db_column=b'status'),
        ),
        migrations.AddField(
            model_name='keyschool',
            name='org',
            field=models.ForeignKey(to='education.Org', db_column=b'org_id'),
        ),
    ]
