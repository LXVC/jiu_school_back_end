# -*- coding:utf-8 -*-
from django.db.models import Model, ForeignKey, CharField, \
    IntegerField, DateTimeField, NullBooleanField, TextField
from .question import Question
from django.contrib.auth.models import User
from education.models import Org


class CodeAssignmentStatus(Model):
    status_name = CharField(max_length=20, default='草稿')

    class Meta:
        app_label = 'question'
        db_table = 'code_assignment_status'


class CodeAssignmentType(Model):
    assignment_type_name = CharField(max_length=50)

    class Meta:
        app_label = 'question'
        db_table = 'code_assignment_type'


class Assignment(Model):
    title = CharField(max_length=30)
    questhion_num = IntegerField(default=2)
    created_by = ForeignKey(User, db_column='created_by', related_name='created_assignment')
    charpter = IntegerField(default=1)
    owner = IntegerField(default=1)
    status = ForeignKey(CodeAssignmentStatus, db_column='status')
    published_count = IntegerField(default=1)
    created_date = DateTimeField(auto_now_add=True)
    type = ForeignKey(CodeAssignmentType, db_column='type')
    comments = CharField(max_length=500, blank=True)

    class Meta:
        app_label = 'question'
        db_table = 'assignment'


class AssignmentPublish(Model):
    assignment = ForeignKey(Assignment, db_column='assignment_id')
    publisher = ForeignKey(User, db_column='publisher')
    reciver_org = ForeignKey(Org, db_column='reciver_org')
    share = NullBooleanField(default=False)
    publish_date = DateTimeField(blank=True)
    publish_date_start = DateTimeField(blank=True)
    publish_date_end = DateTimeField(blank=True)
    comments = CharField(max_length=500, blank=True)

    class Meta:
        app_label = 'question'
        db_table = 'assignment_publish'


class CodeSubmitStatus(Model):
    stastus = (('未做', '未做'),
               ('完成', '完成'),
               ('草稿', '草稿'),
               ('过期', '过期'),)
    submit_status_name = CharField(choices=stastus)

    class Meta:
        app_label = 'question'
        db_table = 'code_submit_status'


class AssignmentSubmit(Model):
    assignment_publish = ForeignKey(AssignmentPublish, db_column='assignment_publish')
    context = TextField()
    submiter = ForeignKey(User, db_column='submiter')
    status = ForeignKey(CodeSubmitStatus, db_column='status')
    start_date = DateTimeField(blank=True)
    submit_date = DateTimeField(blank=True)
    comment = CharField(max_length=500, blank=True)

    class Meta:
        app_label = 'question'
        db_table = 'assignment_submit'


class AssignmentSubmitDetail(Model):
    submit = ForeignKey(AssignmentSubmit, db_column='submit_id')
    question = ForeignKey(Question, db_column='question_id')
    context = CharField(max_length=500, blank=True)
    checking_status = CharField(max_length=20, blank=True)
    checking_context = CharField(max_length=500, blank=True)
    checking_date = DateTimeField()
    checking_by = ForeignKey(User, db_column='checking_by')
    checking_comments = CharField(max_length=500, blank=True)
    status = CharField(max_length=20, blank=True)

    class Meta:
        app_label = 'question'
        db_table = 'assignment_submit_detail'
