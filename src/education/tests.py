# -*- coding:utf-8 -*-
from django.test import TestCase
from .models.user_desc import CodeRole
from django.contrib.auth.models import User

role = CodeRole(role_name='老师')
role.save()

User.objects.create_superuser('root', '403381161@qq.com', 'root')
User.objects.create_user('qzw', '403381161@qq.com','root')
User.objects.create_user('qwer', '403381161@qq.com','root')


