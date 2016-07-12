# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, IntegerField, BooleanField, EmailField, DateField, DateTimeField,\
    ForeignKey, OneToOneField
from django.contrib.auth.models import User
from .user_desc import CodeAccountType, CodeRole, CodeUserStatus
from .org import Org
from django.contrib.auth.models import AbstractUser, Group, Permission


class Profile(Model):
    # 用户表
    user = OneToOneField(User, db_column='id', primary_key=True)
    account_id = CharField(max_length=100)
    account_type = ForeignKey(CodeAccountType, db_column='account_type')
    role = ForeignKey(CodeRole, db_column='role')
    username = CharField(max_length=50)
    login_name = CharField(max_length=50)
    md5passwdstr = CharField(max_length=300, blank=True)
    status = ForeignKey(CodeUserStatus, db_column="status")
    org_id = ForeignKey(Org, db_column='org_id')
    gender = BooleanField()
    email = EmailField()
    phone = CharField(max_length=30)
    birthday = DateField()
    idcardnum = CharField(max_length=30)
    address = CharField(max_length=200)
    intro = CharField(max_length=500)
    qq = CharField(max_length=20)
    wechat = CharField(max_length=100)
    inschoolyears = IntegerField()
    create_date = DateTimeField(auto_now_add=True)
    last_login_date = DateTimeField()
    last_status_change_date = DateTimeField()
    permissgroucp = IntegerField()
    head_pic_url = CharField(max_length=1000)
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


