# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, IntegerField, ForeignKey, FloatField, SmallIntegerField, DateTimeField


class Area(Model):
    # 地区表
    parent = ForeignKey('self', db_column='parent_id', null=True, blank=True)
    path = CharField(max_length=200)
    name = CharField(max_length=50)
    short_name = CharField(max_length=50)
    longitude = FloatField()
    latitude = FloatField()
    level = SmallIntegerField()
    sort = IntegerField()
    status = SmallIntegerField()

    class Meta:
        app_label = 'education'
        db_table = 'area'


class CodeEduPeriod(Model):
    # 学段类别表
    edu_period_name = CharField(max_length=20)

    class Meta:
        app_label = 'education'
        db_table = 'code_edu_period'


class Org(Model):
    # 组织模型表
    parent = ForeignKey('self', db_column='parent_id', null=True, blank=True)
    area = ForeignKey(Area, db_column='area_id')
    name = CharField(max_length=50)
    edu_period = ForeignKey(CodeEduPeriod, db_column='edu_period')
    size = IntegerField()
    path = CharField(max_length=200)
    level = SmallIntegerField()
    sort = IntegerField()
    status = SmallIntegerField()
    created_date = DateTimeField()
    comments = CharField(max_length=500, blank=True)

    class Meta:
        app_label = 'education'
        db_table = 'org'


class KeySchool(Model):
    # 重点学校
    org = ForeignKey(Org, db_column='org_id')
    type = IntegerField()

    class Meta:
        app_label = 'education'
        db_table = 'keyschool'
