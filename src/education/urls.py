from django.conf.urls import url
from rest_framework import routers
from education.api import UsersViewSet
router = routers.DefaultRouter()

router.register(r'users', UsersViewSet)


urlpatterns = router.urls
