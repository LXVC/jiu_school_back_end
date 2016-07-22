# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, IntegerField, ForeignKey, \
    FloatField, SmallIntegerField, DateTimeField


class Area(Model):
    # 地区表
    parent = ForeignKey('self', db_column='parent_id', null=True, blank=True)
    path = CharField(max_length=200, blank=True)
    name = CharField(max_length=50, blank=True)
    short_name = CharField(max_length=50, blank=True)
    longitude = FloatField(blank=True, default=1.1)
    latitude = FloatField(blank=True, default=2.2)
    level = SmallIntegerField(blank=True, default=4)
    sort = IntegerField(blank=True, default=1)
    status = SmallIntegerField(blank=True, default=2)

    class Meta:
        app_label = 'education'
        db_table = 'area'


class CodeEduPeriod(Model):
    # 学段类别表
    edu_period_name = CharField(max_length=20, blank=True, default='小学')

    class Meta:
        app_label = 'education'
        db_table = 'code_edu_period'


class Org(Model):
    # 组织模型表
    parent = ForeignKey('self', db_column='parent_id', null=True, blank=True)
    area = ForeignKey(Area, db_column='area_id')
    name = CharField(max_length=50, blank=True, default='XX中学')
    edu_period = ForeignKey(CodeEduPeriod, db_column='edu_period')
    size = IntegerField(blank=True, default=1200)
    path = CharField(max_length=200, default='湖南', blank=True)
    level = SmallIntegerField(blank=True, default=1)
    type = CharField(max_length=10, default='')
    sort = IntegerField(blank=True, default=2)
    status = SmallIntegerField(default=0, blank=2)
    created_date = DateTimeField(blank=True, auto_now_add=True)
    comments = CharField(max_length=500, blank=True)

    class Meta:
        app_label = 'education'
        db_table = 'org'


class KeySchool(Model):
    # 重点学校
    org = ForeignKey(Org, db_column='org_id')
    type = IntegerField(blank=True, default=10)

    class Meta:
        app_label = 'education'
        db_table = 'keyschool'
