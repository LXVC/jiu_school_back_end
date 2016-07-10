# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, IntegerField, BooleanField, EmailField, DateField, DateTimeField,ForeignKey
from .user_desc import CodeAccountType, CodeRole, CodeUserStatus
from .org import Org


class User(Model):
    # 用户表
    id = IntegerField(primary_key=True)
    account_id = CharField(max_length=100)
    account_type = ForeignKey(CodeAccountType, db_column='account_type')
    role = ForeignKey(CodeRole, db_column='role')
    username = CharField(max_length=50)
    login_name = CharField(max_length=50)
    md5passwdstr = CharField(max_length=300)
    status = ForeignKey(CodeUserStatus, db_column="status")
    org_id = ForeignKey(Org, db_column='org_id')
    geder = BooleanField()
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
    comments = CharField(max_length=500)

    class Meta:
        app_label = 'education'
        db_table = 'user'
