# -*- coding:utf-8 -*-
from hashlib import md5
from django.db.models import Model, CharField, IntegerField, BooleanField, EmailField, DateField, DateTimeField,ForeignKey
from .user_desc import CodeAccountType, CodeRole, CodeUserStatus
from .org import Org


class User(Model):
    # 用户表
    account_id = CharField(max_length=100)
    account_type = ForeignKey(CodeAccountType, db_column='account_type')
    role = ForeignKey(CodeRole, db_column='role')
    username = CharField(max_length=50)
    login_name = CharField(max_length=50)
    md5passwdstr = CharField(max_length=300)
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

    @property
    def md5passwdstr(self):
        raise AttributeError('No Passwd')

    @md5passwdstr.setter
    def md5passwdstr(self, passwd):
        md = md5('qzw')
        md.update(passwd)
        self.md5passwdstr = md.hexdigest()

    def verify_password(self, passwd):
        md = md5('qzw')
        md.update(passwd)
        if md.hexdigest() is self.md5passwdstr:
            return True
        else:
            return False

    class Meta:
        app_label = 'education'
        db_table = 'user'
