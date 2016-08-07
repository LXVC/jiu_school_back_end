# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
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
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('short_name', models.CharField(max_length=50, verbose_name=b'\xe7\xae\x80\xe7\xa7\xb0', blank=True)),
                ('longitude', models.FloatField(default=1.1, null=True, verbose_name=b'\xe7\xbb\x8f\xe5\xba\xa6', blank=True)),
                ('latitude', models.FloatField(default=2.2, null=True, verbose_name=b'\xe7\xba\xac\xe5\xba\xa6', blank=True)),
                ('sort', models.IntegerField(default=1, blank=True)),
                ('status', models.SmallIntegerField(default=2, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', db_column=b'parent_id', blank=True, to='education.Area', null=True, verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7')),
            ],
            options={
                'db_table': 'area',
                'verbose_name': '\u5730\u533a',
                'verbose_name_plural': '\u5730\u533a',
            },
        ),
        migrations.CreateModel(
            name='CodeAccountType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acc_type_name', models.CharField(default='\u624b\u673a\u53f7', max_length=20, verbose_name=b'\xe5\xb8\x90\xe5\x8f\xb7\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('comments', models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'db_table': 'code_account_type',
                'verbose_name': '\u7528\u6237\u8d26\u53f7\u7c7b\u578b',
                'verbose_name_plural': '\u7528\u6237\u8d26\u53f7\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='CodeEduPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edu_period_name', models.CharField(default=b'\xe4\xb8\xad\xe5\xad\xa6', max_length=20, verbose_name=b'\xe5\xad\xa6\xe6\xae\xb5', blank=True)),
            ],
            options={
                'db_table': 'code_edu_period',
                'verbose_name': '\u5b66\u6bb5',
                'verbose_name_plural': '\u5b66\u6bb5',
            },
        ),
        migrations.CreateModel(
            name='CodeGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade_name', models.CharField(default=b'\xe5\x88\x9d\xe4\xb8\x80', max_length=10, verbose_name=b'\xe5\xb9\xb4\xe7\xba\xa7', blank=True)),
            ],
            options={
                'db_table': 'grades',
                'verbose_name': '\u5e74\u7ea7',
                'verbose_name_plural': '\u5e74\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='CodeRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_name', models.CharField(default='\u5b66\u751f', max_length=20, verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd', blank=True)),
                ('comments', models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'db_table': 'code_role',
                'verbose_name': '\u7528\u6237\u8eab\u4efd',
                'verbose_name_plural': '\u7528\u6237\u8eab\u4efd',
            },
        ),
        migrations.CreateModel(
            name='CodeUserStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_state_name', models.CharField(default='\u5728\u7ebf', max_length=20, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
            ],
            options={
                'db_table': 'code_user_status',
                'verbose_name': '\u7528\u6237\u5e10\u53f7\u72b6\u6001',
                'verbose_name_plural': '\u7528\u6237\u5e10\u53f7\u72b6\u6001',
            },
        ),
        migrations.CreateModel(
            name='KeySchool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=10, verbose_name=b'\xe7\xad\x89\xe7\xba\xa7', blank=True)),
            ],
            options={
                'db_table': 'keyschool',
                'verbose_name': '\u540d\u724c\u5b66\u6821',
                'verbose_name_plural': '\u540d\u724c\u5b66\u6821',
            },
        ),
        migrations.CreateModel(
            name='KeyTeacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=10, verbose_name=b'\xe7\xad\x89\xe7\xba\xa7', blank=True)),
                ('details', models.CharField(default=b'', max_length=20, blank=True)),
            ],
            options={
                'db_table': 'keyteacher',
                'verbose_name': '\u540d\u724c\u6559\u5e08',
                'verbose_name_plural': '\u540d\u724c\u6559\u5e08',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20, verbose_name=b'\xe4\xb8\xbb\xe9\xa2\x98')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f')),
                ('content', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
                'db_table': 'notices',
                'verbose_name': '\u516c\u544a',
                'verbose_name_plural': '\u516c\u544a',
            },
        ),
        migrations.CreateModel(
            name='NoticeTo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notice', models.ForeignKey(to='education.Notice', db_column=b'notice_id')),
            ],
            options={
                'db_table': 'notice_to',
                'verbose_name': '\u516c\u544a\u63a5\u6536\u4eba\u6216\u8005\u7ec4\u7ec7',
                'verbose_name_plural': '\u516c\u544a\u63a5\u6536\u4eba\u6216\u8005\u7ec4\u7ec7',
            },
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'XX\xe4\xb8\xad\xe5\xad\xa6', max_length=50, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('size', models.IntegerField(default=1200, verbose_name=b'\xe6\x80\xbb\xe4\xba\xba\xe6\x95\xb0', blank=True)),
                ('type', models.CharField(default=b'\xe5\xad\xa6\xe6\xa0\xa1', max_length=10, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('sort', models.IntegerField(default=2, blank=True)),
                ('status', models.SmallIntegerField(default=0, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=2)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f')),
                ('comments', models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('area', models.ForeignKey(db_column=b'area_id', verbose_name=b'\xe5\x9c\xb0\xe5\x8c\xba', to='education.Area')),
                ('edu_period', models.ForeignKey(db_column=b'edu_period', verbose_name=b'\xe5\xad\xa6\xe6\xae\xb5', to='education.CodeEduPeriod')),
                ('grade', models.ForeignKey(db_column=b'grade', blank=True, to='education.CodeGrade', null=True, verbose_name=b'\xe5\xb9\xb4\xe7\xba\xa7')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', db_column=b'parent_id', blank=True, to='education.Org', null=True, verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7\xe7\xbb\x84\xe7\xbb\x87')),
            ],
            options={
                'db_table': 'org',
                'verbose_name': '\u7ec4\u7ec7',
                'verbose_name_plural': '\u7ec4\u7ec7',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(related_name='profile', primary_key=True, db_column=b'id', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7')),
                ('account_id', models.CharField(max_length=100, blank=True)),
                ('username', models.CharField(max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xa7\x93\xe5\x90\x8d', blank=True)),
                ('login_name', models.CharField(max_length=50, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0', blank=True)),
                ('md5passwdstr', models.CharField(max_length=300, blank=True)),
                ('gender', models.BooleanField(default=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('phone', models.CharField(max_length=30, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7', blank=True)),
                ('birthday', models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5', blank=True)),
                ('idcardnum', models.CharField(max_length=30, verbose_name=b'', blank=True)),
                ('address', models.CharField(max_length=200, verbose_name=b'\xe5\xae\xb6\xe5\xba\xad\xe4\xbd\x8f\xe5\x9d\x80', blank=True)),
                ('intro', models.CharField(max_length=500, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xae\x80\xe4\xbb\x8b', blank=True)),
                ('qq', models.CharField(max_length=20, verbose_name=b'QQ', blank=True)),
                ('wechat', models.CharField(max_length=100, verbose_name=b'\xe5\xbe\xae\xe4\xbf\xa1', blank=True)),
                ('inschoolyears', models.IntegerField(default=2013, verbose_name=b'\xe5\x85\xa5\xe5\xad\xa6\xe5\xb9\xb4\xe4\xbb\xbd', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_login_date', models.DateTimeField(blank=True)),
                ('last_status_change_date', models.DateTimeField(blank=True)),
                ('head_pic_url', models.CharField(max_length=1000, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
                ('comments', models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'db_table': 'user',
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
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
                ('org', models.ForeignKey(db_column=b'org_id', verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87', to='education.Org')),
                ('user', models.ForeignKey(db_column=b'user_id', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_org',
                'verbose_name': '\u7528\u6237\u548c\u7ec4\u7ec7\u7684\u5173\u7cfb',
                'verbose_name_plural': '\u7528\u6237\u548c\u7ec4\u7ec7\u7684\u5173\u7cfb',
            },
        ),
        migrations.CreateModel(
            name='UserPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permission', models.ForeignKey(db_column=b'permission_id', default=1, verbose_name=b'\xe6\x9d\x83\xe9\x99\x90', to='auth.Permission')),
            ],
            options={
                'db_table': 'user_permissions',
                'verbose_name': '\u7528\u6237\u4e0e\u6743\u9650',
                'verbose_name_plural': '\u7528\u6237\u4e0e\u6743\u9650',
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
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.FloatField(verbose_name=b'\xe7\x89\x88\xe6\x9c\xac')),
                ('url', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe5\x9c\xb0\xe5\x9d\x80')),
                ('comments', models.TextField(verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe5\x86\x85\xe5\xae\xb9')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
            options={
                'db_table': 'version',
                'verbose_name': 'APP \u7248\u672c',
                'verbose_name_plural': 'APP \u7248\u672c',
            },
        ),
        migrations.CreateModel(
            name='UserRelationInfo',
            fields=[
                ('user', models.OneToOneField(primary_key=True, db_column=b'user_id', serialize=False, to='education.Profile', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7')),
                ('relation_type', models.CharField(default=b'\xe7\x88\xb6\xe4\xba\xb2', max_length=10, verbose_name=b'\xe5\x85\xb3\xe7\xb3\xbb', blank=True)),
                ('relation_name', models.CharField(default=b'\xe6\x9d\x8e\xe5\xa4\xa9\xe4\xb8\x80', max_length=50, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d', blank=True)),
                ('relation_phone', models.CharField(default=b'13788740727', max_length=32, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7')),
                ('relation_email', models.EmailField(default=b'403381161@qq.com', max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('relation_address', models.CharField(default=b'\xe6\xb9\x96\xe5\x8d\x97', max_length=200, verbose_name=b'\xe5\xae\xb6\xe5\xba\xad\xe4\xbd\x8f\xe5\x9d\x80')),
                ('comments', models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'db_table': 'user_relation_info',
                'verbose_name': '\u7528\u6237\u4eb2\u5c5e\u5173\u7cfb',
                'verbose_name_plural': '\u7528\u6237\u4eb2\u5c5e\u5173\u7cfb',
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
            field=models.ForeignKey(db_column=b'user_id', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to='education.Profile'),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='user',
            field=models.ForeignKey(to='education.Profile', db_column=b'user_id'),
        ),
        migrations.AddField(
            model_name='profile',
            name='account_type',
            field=models.ForeignKey(db_column=b'account_type', verbose_name=b'\xe5\xb8\x90\xe5\x8f\xb7\xe7\xb1\xbb\xe5\x9e\x8b', to='education.CodeAccountType'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(db_column=b'role', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe8\xba\xab\xe4\xbb\xbd', to='education.CodeRole'),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.ForeignKey(db_column=b'status', verbose_name=b'\xe5\xb8\x90\xe5\x8f\xb7\xe7\x8a\xb6\xe6\x80\x81', to='education.CodeUserStatus'),
        ),
        migrations.AddField(
            model_name='noticeto',
            name='org',
            field=models.ForeignKey(related_name='notices', db_column=b'org_id', blank=True, to='education.Org', null=True),
        ),
        migrations.AddField(
            model_name='noticeto',
            name='user',
            field=models.ForeignKey(related_name='notices', db_column=b'user_id', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='created_by',
            field=models.ForeignKey(related_name='created_notices', db_column=b'create_by', verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe4\xba\xba', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='keyteacher',
            name='teacher',
            field=models.ForeignKey(db_column=b'user_id', verbose_name=b'\xe6\x95\x99\xe5\xb8\x88', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='keyschool',
            name='org',
            field=models.ForeignKey(db_column=b'org_id', verbose_name=b'\xe5\xad\xa6\xe6\xa0\xa1', to='education.Org'),
        ),
    ]
