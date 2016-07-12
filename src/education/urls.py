from django.conf.urls import url
from rest_framework import routers
from .views import UserList

router = routers.DefaultRouter()

router.register(r'users', UserList)

urlpatterns = router.urls
