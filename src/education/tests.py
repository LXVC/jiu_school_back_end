# -*- coding:utf-8 -*-
from django.test import TestCase
from django.utils import timezone
from .models.user_desc import CodeRole, CodeAccountType, CodeUserStatus
from django.contrib.auth.models import User
from .models.user import Profile, UserOrg
from .models.org import Area, CodeEduPeriod, Org, KeySchool
from .models.notice import Notice, NoticeTo

# init Users
User.objects.create_superuser('root', '403381161@qq.com', 'root')
User.objects.create_user('qzw', '403381161@qq.com', 'root')

# init User 身份数据
role = CodeRole(role_name='学生')
role.save()

# init User 账户类型
account_type = CodeAccountType()
account_type.save()

# init User 账户现在的状态
user_status = CodeUserStatus()
user_status.save()

# init Area 数据
area = Area(parent=None, path='中国湖南省衡阳市衡阳县', name='衡阳县', short_name='衡阳', )
area.save()

# init EduPeriod 学段数据
edu_period = CodeEduPeriod()
edu_period.save()

# init Org 组织数据
org = Org(parent=None, area=area, name='衡阳县第一中学', edu_period=edu_period, type='中学')
org.save()

# init 重点中学数据
key_school = KeySchool(org=org)
key_school.save()

# init Profile 用户配置文件
profile = Profile(user=User.objects.get(pk=2), account_id='13788740727', account_type=account_type,
                  role=role, username='qzw', login_name='lxvc', md5passwdstr='md5',
                  status=user_status, email='403381161@qq.com', phone='13788740727',
                  birthday=timezone.now(), idcardnum='...', address='中国湖南省衡阳市衡阳县渣江镇',
                  intro='成绩不错', qq='403381161', wechat='403381161', last_login_date=timezone.now(),
                  last_status_change_date=timezone.now(), head_pic_url='/static/avatar.png')
profile.save()

# init UserOrg 个人和组织的关系数据
user_org = UserOrg(user=User.objects.get(pk=2), org=org)
user_org.save()

# init Notice 通知数据
notice = Notice(title='十一放假通知', created_by=User.objects.get(pk=2), created_date=timezone.now(),
                content='十月一号开始放假七天')
notice.save()

# init NoticeTo 通知和用户,组织多对多表
notice_to = NoticeTo(notice=notice, org=org)
notice_to.save()
