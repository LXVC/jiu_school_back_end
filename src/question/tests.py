# -*- coding:utf-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from question import models as question_models
from education import models as eduction_models

# 题库
library = question_models.Library(
    library_name=u'初级题库', owner=eduction_models.Org.objects.get(pk=1))
library.save()

# 问题类型
questhion_types = (u'主观题', u'客观题')
for i in questhion_types:
    questhion_type = question_models.CodeQuesthionType(questhion_type_name=i)
    questhion_type.save()

# 回答类型
context_types = (u'文字', u'图片')
for i in context_types:
    context_type = question_models.CodeContextType(context_type_name=i)
    context_type.save()

# 科目
subjects = (u'语文',
            u'数学',
            u'英语',
            u'物理',
            u'化学',
            u'生物',
            u'历史',
            u'地理',
            u'政治')
for i in subjects:
    subject = question_models.CodeSubject(subject_name=i)
    subject.save()

# 章节
charpter = question_models.Charpter(title=u'第一章', subject=question_models.CodeSubject.objects.get(pk=1),
                                    parent=None, owner=eduction_models.Org.objects.get(pk=1))
charpter.save()

# 知识点
knowege_point = question_models.KnowegePoint(title=u'三角函数', parent=None, created_by=User.objects.get(pk=1),
                                             owner=eduction_models.Org.objects.get(pk=1))
knowege_point.save()

# 作业状态
assignment_status = [u'草稿', u'正式', u'作废']
for i in assignment_status:
    assignment_statu = question_models.CodeAssignmentStatus(status_name=i)
    assignment_statu.save()

# 作业类型
assignment_types = [u'日常作业', u'游学名校', u'寒假作业']
for i in assignment_types:
    assignment_type = question_models.CodeAssignmentType(
        assignment_type_name=i)
    assignment_type.save()

# 作业提交状态
submit_status = (u'完成', u'草稿')
for i in submit_status:
    submit_statu = question_models.CodeSubmitStatus(submit_status_name=i)
    submit_statu.save()
