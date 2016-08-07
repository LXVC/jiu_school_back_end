# -*- coding:utf-8 -*-
from django.test import TestCase
from question import models

assignment_status = [u'草稿', u'正式', u'作废']

for i in assignment_status:
    assignment_statu = models.CodeAssignmentStatus(status_name=i)
    assignment_statu.save()
