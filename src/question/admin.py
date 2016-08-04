from django.contrib import admin
from question import models

admin.site.register(models.Question)
admin.site.register(models.Material)
admin.site.register(models.Library)
admin.site.register(models.CodeQuesthionType)
admin.site.register(models.CodeContextType)
admin.site.register(models.CodeSubject)
admin.site.register(models.Charpter)
admin.site.register(models.QuestionsDyndifficulty)
admin.site.register(models.KnowegePoint)
admin.site.register(models.QuestionKnowlegePoint)
admin.site.register(models.WeakPoint)
admin.site.register(models.CodeAssignmentStatus)
admin.site.register(models.CodeAssignmentType)
admin.site.register(models.Assignment)
admin.site.register(models.AssignmentPublish)
admin.site.register(models.CodeSubmitStatus)
admin.site.register(models.AssignmentSubmit)
admin.site.register(models.AssignmentSubmitDetail)
