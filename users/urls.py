from rest_framework import routers
from users.views import ApiUser
from users.views import ArticlesViewSet
from users.views import my

router = routers.DefaultRouter()
# 第一个参数为url前缀，第二个参数是前缀对应的试图集，第三个参数是视图基本名
router.register('userapi', ApiUser, basename='userapi')
router.register('ArticlesViewSet', ArticlesViewSet, basename='ArticlesViewSet')
router.register('my', my, basename='my')
urlpatterns = []

urlpatterns += router.urls
