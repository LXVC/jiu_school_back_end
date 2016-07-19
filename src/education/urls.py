from django.conf.urls import url
from rest_framework import routers
from education.api import UsersViewSet
router = routers.DefaultRouter()

router.register(r'users', UsersViewSet, 'Users')
# router.register(r'^users/(?P<pk>[0-9]+)/$', UsersViewSet.as_view({'get': 'list'}))
url(r'^users/(?P<pk>[0-9]+)/$', UsersViewSet.as_view({'get': 'list'}), name='user')

urlpatterns = router.urls
