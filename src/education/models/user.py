# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, IntegerField


# Create your models here.

class User(Model):
    # 用户表
    id = IntegerField(primary_key=True)
    account_id = CharField(max_length=100)

    class Meta:
        app_label = 'education'
        db_table = 'user'
