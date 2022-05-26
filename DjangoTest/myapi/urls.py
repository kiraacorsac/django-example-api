from django.db import router
from django.urls import path, include


from rest_framework import routers
from myapi.views import MonsterViewSet

router = routers.DefaultRouter()
 # monsters will be accessible on http://<myapi>/monsters/
router.register('monsters', MonsterViewSet)

urlpatterns = [
    path('', include(router.urls))
]