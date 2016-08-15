# -*- coding:utf-8 -*-
from rest_framework import permissions
from education import models as education_models
from question import models as question_models


class HasHomeWork(permissions.BasePermission):
    def has_permission(self, request, view):
        user_orgs_relation = education_models.UserOrg.objects.filter(user=request.user)