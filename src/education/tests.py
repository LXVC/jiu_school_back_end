# -*- coding:utf-8 -*-
from django.test import TestCase
from django.utils import timezone
from .models.user_desc import CodeRole, CodeAccountType, CodeUserStatus
from django.contrib.auth.models import User
from .models.user import Profile, UserOrg, KeyTeacher
from .models.org import Area, CodeEduPeriod, Org, KeySchool, CodeOrgType
from .models.notice import Notice, NoticeTo

# init Users
User.objects.create_superuser('root', '403381161@qq.com', 'root')
User.objects.create_user('qzw', '403381161@qq.com', 'root')
User.objects.create_user('teacher', '403381161@qq.com', 'teacher')
User.objects.create_user('student', '403381161@qq.com', 'student')

# init User 身份数据
roles = [u'教务', u'教师', u'学生']
for r in roles:
    role = CodeRole(role_name=r)
    role.save()

# init User 账户类型
account_type = CodeAccountType()
account_type.save()

# init User 账户现在的状态
user_status = CodeUserStatus()
user_status.save()

# init Area 数据
area = Area(parent=None, name=u'衡阳县', short_name=u'衡阳', )
area.save()

# init EduPeriod 学段数据
edu_period = CodeEduPeriod()
edu_period.save()

# init OrgType
types = [u'学校', u'班级', u'小组']
for i in types:
    ty_pe = CodeOrgType(org_type_name=i)
    ty_pe.save()

# init Org 组织数据
org = Org(parent=None, area=area, name=u'衡阳县第一中学',
          edu_period=edu_period, type_id=1)
org.save()

# init Profile 用户配置文件
for i in [2, 3, 4]:
    profile = Profile(user=User.objects.get(pk=i), account_id='13788740727', account_type=account_type,
                      role_id=i - 1, username='qzw', login_name='lxvc', md5passwdstr='md5',
                      status=user_status, email='403381161@qq.com', phone='13788740727',
                      birthday=timezone.now(), idcardnum='...', address=u'中国湖南省衡阳市衡阳县渣江镇',
                      intro=u'成绩不错', qq='403381161', wechat='403381161', last_login_date=timezone.now(),
                      last_status_change_date=timezone.now(), head_pic_url='/static/avatar.png')
    profile.save()

# init UserOrg 个人和组织的关系数据
user_org = UserOrg(user=User.objects.get(pk=2), org=org)
user_org.save()

# init Notice 通知数据
notice = Notice(title=u'十一放假通知', created_by=User.objects.get(pk=2), created_date=timezone.now(),
                content=u'十月一号开始放假七天')
notice.save()

# init NoticeTo 通知和用户,组织多对多表
notice_to = NoticeTo(notice=notice, org=org)
notice_to.save()

# init Keyschool 名校数据
school = KeySchool(org=org)
school.save()

# init Keyteacher 名师数据
teacher = KeyTeacher(teacher=User.objects.get(pk=1), details=u'湖南特级教师')
teacher.save()
