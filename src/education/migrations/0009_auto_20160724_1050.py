# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_auto_20160724_0728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': '\u5730\u533a', 'verbose_name_plural': '\u5730\u533a'},
        ),
        migrations.AlterModelOptions(
            name='codeaccounttype',
            options={'verbose_name': '\u7528\u6237\u8d26\u53f7\u7c7b\u578b', 'verbose_name_plural': '\u7528\u6237\u8d26\u53f7\u7c7b\u578b'},
        ),
        migrations.AlterModelOptions(
            name='codeeduperiod',
            options={'verbose_name': '\u5b66\u6bb5', 'verbose_name_plural': '\u5b66\u6bb5'},
        ),
        migrations.AlterModelOptions(
            name='coderole',
            options={'verbose_name': '\u7528\u6237\u8eab\u4efd', 'verbose_name_plural': '\u7528\u6237\u8eab\u4efd'},
        ),
        migrations.AlterModelOptions(
            name='codeuserstatus',
            options={'verbose_name': '\u7528\u6237\u5e10\u53f7\u72b6\u6001', 'verbose_name_plural': '\u7528\u6237\u5e10\u53f7\u72b6\u6001'},
        ),
        migrations.AlterModelOptions(
            name='keyschool',
            options={'verbose_name': '\u91cd\u70b9\u5b66\u6821', 'verbose_name_plural': '\u91cd\u70b9\u5b66\u6821'},
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'verbose_name': '\u516c\u544a', 'verbose_name_plural': '\u516c\u544a'},
        ),
        migrations.AlterModelOptions(
            name='noticeto',
            options={'verbose_name': '\u516c\u544a\u63a5\u6536\u4eba\u6216\u8005\u7ec4\u7ec7', 'verbose_name_plural': '\u516c\u544a\u63a5\u6536\u4eba\u6216\u8005\u7ec4\u7ec7'},
        ),
        migrations.AlterModelOptions(
            name='org',
            options={'verbose_name': '\u7ec4\u7ec7', 'verbose_name_plural': '\u7ec4\u7ec7'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': '\u7528\u6237\u4fe1\u606f', 'verbose_name_plural': '\u7528\u6237\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='userorg',
            options={'verbose_name': '\u7528\u6237\u548c\u7ec4\u7ec7\u7684\u5173\u7cfb', 'verbose_name_plural': '\u7528\u6237\u548c\u7ec4\u7ec7\u7684\u5173\u7cfb'},
        ),
        migrations.AlterModelOptions(
            name='userpermissions',
            options={'verbose_name': '\u7528\u6237\u4e0e\u6743\u9650', 'verbose_name_plural': '\u7528\u6237\u4e0e\u6743\u9650'},
        ),
        migrations.AlterModelOptions(
            name='userrelationinfo',
            options={'verbose_name': '\u7528\u6237\u4eb2\u5c5e\u5173\u7cfb', 'verbose_name_plural': '\u7528\u6237\u4eb2\u5c5e\u5173\u7cfb'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='org',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='permissgroucp',
        ),
        migrations.AlterField(
            model_name='area',
            name='latitude',
            field=models.FloatField(default=2.2, null=True, verbose_name='\u7eac\u5ea6', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='level',
            field=models.SmallIntegerField(default=4, verbose_name='\u7ea7\u522b', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='longitude',
            field=models.FloatField(default=1.1, null=True, verbose_name='\u7ecf\u5ea6', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u540d\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='parent',
            field=models.ForeignKey(db_column=b'parent_id', blank=True, to='education.Area', null=True, verbose_name='\u4e0a\u7ea7'),
        ),
        migrations.AlterField(
            model_name='area',
            name='path',
            field=models.CharField(max_length=200, verbose_name='\u5177\u4f53\u4f4d\u7f6e', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='short_name',
            field=models.CharField(max_length=50, verbose_name='\u7b80\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='status',
            field=models.SmallIntegerField(default=2, verbose_name='\u72b6\u6001', blank=True),
        ),
        migrations.AlterField(
            model_name='codeaccounttype',
            name='acc_type_name',
            field=models.CharField(default='\u624b\u673a\u53f7', max_length=20, verbose_name=b'\xe5\xb8\x90\xe5\x8f\xb7\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='codeaccounttype',
            name='comments',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='codeeduperiod',
            name='edu_period_name',
            field=models.CharField(default=b'\xe4\xb8\xad\xe5\xad\xa6', max_length=20, verbose_name=b'\xe5\xad\xa6\xe6\xae\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='coderole',
            name='comments',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='coderole',
            name='role_name',
            field=models.CharField(default='\u5b66\u751f', max_length=20, verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd', blank=True),
        ),
        migrations.AlterField(
            model_name='codeuserstatus',
            name='user_state_name',
            field=models.CharField(default='\u5728\u7ebf', max_length=20, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='keyschool',
            name='org',
            field=models.ForeignKey(db_column=b'org_id', verbose_name=b'\xe5\xad\xa6\xe6\xa0\xa1', to='education.Org'),
        ),
        migrations.AlterField(
            model_name='keyschool',
            name='type',
            field=models.IntegerField(default=10, verbose_name=b'\xe7\xad\x89\xe7\xba\xa7', blank=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='created_by',
            field=models.ForeignKey(related_name='created_notices', db_column=b'create_by', verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe4\xba\xba', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notice',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=20, verbose_name=b'\xe4\xb8\xbb\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='org',
            name='area',
            field=models.ForeignKey(db_column=b'area_id', verbose_name=b'\xe5\x9c\xb0\xe5\x8c\xba', to='education.Area'),
        ),
        migrations.AlterField(
            model_name='org',
            name='comments',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='org',
            name='edu_period',
            field=models.ForeignKey(db_column=b'edu_period', verbose_name=b'\xe5\xad\xa6\xe6\xae\xb5', to='education.CodeEduPeriod'),
        ),
        migrations.AlterField(
            model_name='org',
            name='level',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xe7\xba\xa7\xe5\x88\xab', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='name',
            field=models.CharField(default=b'XX\xe4\xb8\xad\xe5\xad\xa6', max_length=50, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='parent',
            field=models.ForeignKey(db_column=b'parent_id', blank=True, to='education.Org', null=True, verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7\xe7\xbb\x84\xe7\xbb\x87'),
        ),
        migrations.AlterField(
            model_name='org',
            name='path',
            field=models.CharField(default=b'\xe6\xb9\x96\xe5\x8d\x97', max_length=200, verbose_name=b'\xe5\x85\xb7\xe4\xbd\x93\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='size',
            field=models.IntegerField(default=1200, verbose_name=b'\xe6\x80\xbb\xe4\xba\xba\xe6\x95\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='status',
            field=models.SmallIntegerField(default=0, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=2),
        ),
        migrations.AlterField(
            model_name='org',
            name='type',
            field=models.CharField(default=b'\xe5\xad\xa6\xe6\xa0\xa1', max_length=10, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='account_type',
            field=models.ForeignKey(db_column=b'account_type', verbose_name=b'\xe5\xb8\x90\xe5\x8f\xb7\xe7\xb1\xbb\xe5\x9e\x8b', to='education.CodeAccountType'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=200, verbose_name=b'\xe5\xae\xb6\xe5\xba\xad\xe4\xbd\x8f\xe5\x9d\x80', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='comments',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='head_pic_url',
            field=models.CharField(max_length=1000, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='idcardnum',
            field=models.CharField(max_length=30, verbose_name=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='inschoolyears',
            field=models.IntegerField(default=2013, verbose_name=b'\xe5\x85\xa5\xe5\xad\xa6\xe5\xb9\xb4\xe4\xbb\xbd', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='intro',
            field=models.CharField(max_length=500, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xae\x80\xe4\xbb\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='login_name',
            field=models.CharField(max_length=50, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=30, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='qq',
            field=models.CharField(max_length=20, verbose_name=b'QQ', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(db_column=b'role', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe8\xba\xab\xe4\xbb\xbd', to='education.CodeRole'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.ForeignKey(db_column=b'status', verbose_name=b'\xe5\xb8\x90\xe5\x8f\xb7\xe7\x8a\xb6\xe6\x80\x81', to='education.CodeUserStatus'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name='profile', primary_key=True, db_column=b'id', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xa7\x93\xe5\x90\x8d', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wechat',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\xbe\xae\xe4\xbf\xa1', blank=True),
        ),
        migrations.AlterField(
            model_name='userorg',
            name='org',
            field=models.ForeignKey(db_column=b'org_id', verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87', to='education.Org'),
        ),
        migrations.AlterField(
            model_name='userorg',
            name='user',
            field=models.ForeignKey(db_column=b'user_id', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userpermissions',
            name='permission',
            field=models.ForeignKey(db_column=b'permission_id', default=1, verbose_name=b'\xe6\x9d\x83\xe9\x99\x90', to='auth.Permission'),
        ),
        migrations.AlterField(
            model_name='userpermissions',
            name='user',
            field=models.ForeignKey(db_column=b'user_id', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to='education.Profile'),
        ),
        migrations.AlterField(
            model_name='userrelationinfo',
            name='comments',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='userrelationinfo',
            name='relation_address',
            field=models.CharField(default=b'\xe6\xb9\x96\xe5\x8d\x97', max_length=200, verbose_name=b'\xe5\xae\xb6\xe5\xba\xad\xe4\xbd\x8f\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='userrelationinfo',
            name='relation_email',
            field=models.EmailField(default=b'403381161@qq.com', max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True),
        ),
        migrations.AlterField(
            model_name='userrelationinfo',
            name='relation_name',
            field=models.CharField(default=b'\xe6\x9d\x8e\xe5\xa4\xa9\xe4\xb8\x80', max_length=50, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d', blank=True),
        ),
        migrations.AlterField(
            model_name='userrelationinfo',
            name='relation_phone',
            field=models.CharField(default=b'13788740727', max_length=32, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='userrelationinfo',
            name='relation_type',
            field=models.CharField(default=b'\xe7\x88\xb6\xe4\xba\xb2', max_length=10, verbose_name=b'\xe5\x85\xb3\xe7\xb3\xbb', blank=True),
        ),
        migrations.AlterField(
            model_name='userrelationinfo',
            name='user',
            field=models.OneToOneField(primary_key=True, db_column=b'user_id', serialize=False, to='education.Profile', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7'),
        ),
    ]
