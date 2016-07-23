# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, IntegerField, \
    BooleanField, EmailField, DateField, DateTimeField, ForeignKey, OneToOneField
from django.contrib.auth.models import User
from .user_desc import CodeAccountType, CodeRole, CodeUserStatus
from .org import Org


class Profile(Model):
    # 用户配置表
    user = OneToOneField(User, db_column='id', primary_key=True, related_name='profile')
    account_id = CharField(max_length=100, blank=True)
    account_type = ForeignKey(CodeAccountType, db_column='account_type')
    role = ForeignKey(CodeRole, db_column='role')
    username = CharField(max_length=50, blank=True)
    login_name = CharField(max_length=50, blank=True)
    md5passwdstr = CharField(max_length=300, blank=True)
    status = ForeignKey(CodeUserStatus, db_column="status")
    org = ForeignKey(Org, db_column='org_id', related_name='users', null=True, blank=True)
    gender = BooleanField(default=True)  # True 为男性
    email = EmailField(blank=True)
    phone = CharField(max_length=30, blank=True)
    birthday = DateField(blank=True)
    idcardnum = CharField(max_length=30, blank=True)
    address = CharField(max_length=200, blank=True)
    intro = CharField(max_length=500, blank=True)
    qq = CharField(max_length=20, blank=True)
    wechat = CharField(max_length=100, blank=True)
    inschoolyears = IntegerField(blank=True, default=2013)
    create_date = DateTimeField(auto_now_add=True)
    last_login_date = DateTimeField(blank=True)
    last_status_change_date = DateTimeField(blank=True)
    permissgroucp = IntegerField(blank=True, default=2)
    head_pic_url = CharField(max_length=1000, blank=True)
    comments = CharField(max_length=500, blank=True)

    class Meta:
        app_label = 'education'
        db_table = 'user'


class UserOrg(Model):
    # 用户和组织多对多关系表
    user = ForeignKey(User, db_column='user_id')
    org = ForeignKey(Org, db_column='org_id')

    class Meta:
        app_label = 'education'
        db_table = 'user_org'
