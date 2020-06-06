from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()

router.register('users', UserViewSet)
router.register('posts', PostViewSet)

urlpatterns = router.urls
