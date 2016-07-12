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
                ('path', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=50)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('level', models.SmallIntegerField()),
                ('sort', models.IntegerField()),
                ('status', models.SmallIntegerField()),
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
                ('acc_type_name', models.CharField(max_length=20)),
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
                ('edu_period_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'code_edu_period',
            },
        ),
        migrations.CreateModel(
            name='CodeRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_name', models.CharField(max_length=20)),
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
                ('type', models.IntegerField()),
            ],
            options={
                'db_table': 'keyschool',
            },
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('path', models.CharField(max_length=200)),
                ('level', models.SmallIntegerField()),
                ('sort', models.IntegerField()),
                ('status', models.SmallIntegerField()),
                ('created_date', models.DateTimeField()),
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
                ('user', models.OneToOneField(primary_key=True, db_column=b'id', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('account_id', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('login_name', models.CharField(max_length=50)),
                ('md5passwdstr', models.CharField(max_length=300, blank=True)),
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
                ('comments', models.CharField(max_length=500, blank=True)),
                ('account_type', models.ForeignKey(to='education.CodeAccountType', db_column=b'account_type')),
                ('org_id', models.ForeignKey(to='education.Org', db_column=b'org_id')),
                ('role', models.ForeignKey(to='education.CodeRole', db_column=b'role')),
                ('status', models.ForeignKey(to='education.CodeUserStatus', db_column=b'status')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserOrg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('org', models.ForeignKey(to='education.Org', db_column=b'org_id')),
            ],
            options={
                'db_table': 'user_org',
            },
        ),
        migrations.CreateModel(
            name='UserPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permission', models.IntegerField(default=0, db_column=b'permission_id')),
            ],
            options={
                'db_table': 'user_permissions',
            },
        ),
        migrations.CreateModel(
            name='UserRelationInfo',
            fields=[
                ('user', models.OneToOneField(primary_key=True, db_column=b'user_id', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('relation_type', models.CharField(max_length=10)),
                ('relation_name', models.CharField(max_length=50)),
                ('relation_phone', models.CharField(max_length=32)),
                ('relation_email', models.EmailField(max_length=254)),
                ('relation_address', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=500, blank=True)),
            ],
            options={
                'db_table': 'user_relation_info',
            },
        ),
        migrations.CreateModel(
            name='UserStatusChangeLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('change_date', models.DateTimeField()),
                ('resason', models.CharField(max_length=500)),
                ('new_status', models.ForeignKey(related_name='new_status', db_column=b'new_status', to='education.CodeUserStatus')),
                ('old_status', models.ForeignKey(related_name='old_status', db_column=b'old_status', to='education.CodeUserStatus')),
                ('oper', models.ForeignKey(related_name='operator', db_column=b'oper', to=settings.AUTH_USER_MODEL)),
                ('use', models.ForeignKey(related_name='who', db_column=b'user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_status_change_log',
            },
        ),
        migrations.AddField(
            model_name='userpermissions',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'user_id'),
        ),
        migrations.AddField(
            model_name='userorg',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'user_id'),
        ),
        migrations.AddField(
            model_name='keyschool',
            name='org',
            field=models.ForeignKey(to='education.Org', db_column=b'org_id'),
        ),
    ]
