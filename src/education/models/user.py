# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, IntegerField, TextField, \
    BooleanField, EmailField, DateField, DateTimeField, ForeignKey, OneToOneField, FloatField
from django.contrib.auth.models import User
from .user_desc import CodeAccountType, CodeRole, CodeUserStatus
from .org import Org


class Profile(Model):
    # 用户配置表
    user = OneToOneField(User, db_column='id', primary_key=True, related_name='profile', verbose_name='用户')
    account_id = CharField(max_length=100, blank=True)
    account_type = ForeignKey(CodeAccountType, db_column='account_type', verbose_name='帐号类型')
    role = ForeignKey(CodeRole, db_column='role', verbose_name='用户身份')
    username = CharField(max_length=50, blank=True, verbose_name='用户姓名')
    login_name = CharField(max_length=50, blank=True, verbose_name='昵称')
    md5passwdstr = CharField(max_length=300, blank=True)
    status = ForeignKey(CodeUserStatus, db_column="status", verbose_name='帐号状态')
    gender = BooleanField(default=True, verbose_name='性别')  # True 为男性
    email = EmailField(blank=True, verbose_name='邮箱')
    phone = CharField(max_length=30, blank=True, verbose_name='手机号')
    birthday = DateField(blank=True, verbose_name='生日')
    idcardnum = CharField(max_length=30, blank=True, verbose_name='')
    address = CharField(max_length=200, blank=True, verbose_name='家庭住址')
    intro = CharField(max_length=500, blank=True, verbose_name='个人简介')
    qq = CharField(max_length=20, blank=True, verbose_name='QQ')
    wechat = CharField(max_length=100, blank=True, verbose_name='微信')
    inschoolyears = IntegerField(blank=True, default=2013, verbose_name='入学年份')
    create_date = DateTimeField(auto_now_add=True)
    last_login_date = DateTimeField(blank=True)
    last_status_change_date = DateTimeField(blank=True)
    head_pic_url = CharField(max_length=1000, blank=True, verbose_name='头像图片')
    comments = CharField(max_length=500, blank=True, verbose_name='备注')

    class Meta:
        app_label = 'education'
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __unicode__(self):
        return '{0}'.format(self.user.username)


class UserOrg(Model):
    # 用户和组织多对多关系表
    user = ForeignKey(User, db_column='user_id', verbose_name='用户')
    org = ForeignKey(Org, db_column='org_id', verbose_name='组织')
    is_admin = BooleanField(default=False)

    class Meta:
        app_label = 'education'
        db_table = 'user_org'
        verbose_name = '用户和组织的关系'
        verbose_name_plural = '用户和组织的关系'

    def __unicode__(self):
        return u'{0}@{1}'.format(self.user.username, self.org.name)


class KeyTeacher(Model):
    # 名师
    teacher = ForeignKey(User, db_column='user_id', verbose_name='教师')
    type = IntegerField(blank=True, default=10, verbose_name='等级')
    details = CharField(max_length=20, blank=True, default='')

    class Meta:
        app_label = 'education'
        db_table = 'keyteacher'
        verbose_name = '名牌教师'
        verbose_name_plural = '名牌教师'

    def __unicode__(self):
        return u'{0}'.format(self.teacher.username)


class Version(Model):
    version = FloatField(verbose_name='版本')
    url = CharField(max_length=100, verbose_name='下载地址')
    comments = TextField(verbose_name='更新内容')
    created_date = DateTimeField(auto_now_add=True, verbose_name='更新日期')

    class Meta:
        app_label = 'education'
        db_table = 'version'
        verbose_name = 'APP 版本'
        verbose_name_plural = 'APP 版本'

    def __unicode__(self):
        return u'{0}版'.format(self.version)
