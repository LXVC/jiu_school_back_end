from django.contrib import admin
from .models import Profile
from .models.user_desc import CodeUserStatus, CodeAccountType, CodeRole
from .models.org import Org, Area, CodeEduPeriod
from .models.notice import Notice, NoticeTo

admin.site.register(Profile)
admin.site.register(CodeUserStatus)
admin.site.register(CodeAccountType)
admin.site.register(CodeRole)
admin.site.register(Org)
admin.site.register(Area)
admin.site.register(CodeEduPeriod)
admin.site.register(Notice)
admin.site.register(NoticeTo)