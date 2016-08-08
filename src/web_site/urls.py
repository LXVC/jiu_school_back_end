"""web_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from education import api
from question import api as question_api
from question import views as question_view
from rest_framework import routers
from rest_framework.authtoken.models import Token

apiRouter = routers.DefaultRouter()
apiRouter.register(r'users', api.UsersViewSet, 'Users')
apiRouter.register(r'profile', api.UsersProfileViewSet, 'Profile')
apiRouter.register(r'org', api.OrgViewSet, 'Org')
apiRouter.register(r'notices', api.NoticeViewSet, 'Notice')
apiRouter.register(r'version', api.VersionViewSet, 'Version')
apiRouter.register(r'keyteacher', api.KeyTeacherViewSet, 'Keyteacher')
apiRouter.register(r'keyschool', api.KeySchoolViewSet, 'KeySchool')
apiRouter.register(r'charters', question_api.CharpterViewSet, 'Charters')

admin.site.unregister(Token)

urlpatterns = [
    url(r'^$', question_view.index),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/v1/', include(admin.site.urls)),
    url(r'^api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/get-token/', api.CreateToken.as_view()),
    url(r'^api/v1/', include(apiRouter.urls)),
]
