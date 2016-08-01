from django.contrib import admin
from .models import Profile, UserOrg, Version, KeyTeacher, CodeGrade
from .models.user_desc import CodeUserStatus, CodeAccountType, CodeRole
from .models.org import Org, Area, CodeEduPeriod, KeySchool
from .models.notice import Notice, NoticeTo


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(CodeGrade)
admin.site.register(KeySchool)
admin.site.register(KeyTeacher)
admin.site.register(Version)
admin.site.register(UserOrg)
admin.site.register(CodeUserStatus)
admin.site.register(CodeAccountType)
admin.site.register(CodeRole)
admin.site.register(Org)
admin.site.register(Area)
admin.site.register(CodeEduPeriod)
admin.site.register(Notice)
admin.site.register(NoticeTo)
