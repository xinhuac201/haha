from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('', views.LoginViewSet, basename=False)
router.register('',views.SendSmsViewSet,basename=False)
router.register('register',views.RegisterGenericViewSet,basename=False)
# 注册ViewSet的路由
# router.register()

urlpatterns = [
    path('', include(router.urls)),
]
