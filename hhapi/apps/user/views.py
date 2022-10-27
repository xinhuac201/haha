from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from . import serializer
from utils.response import APIResponse
from . import models
from .throttings import SMSSimpleRateThrottle
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from utils.validata import verify_mobile_num


class LoginViewSet(ViewSet):

    @action(methods=['post'], detail=False)
    def login(self, request, *args, **kwargs):
        """
        这个是多合一登录接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ser = serializer.UserModelSerializer(data=request.data, context={'request': request})
        if ser.is_valid():
            token = ser.context.get('token')
            icon = ser.context.get('icon')
            username = ser.context.get('username')
            id = ser.context.get('id')
            data = {
                'token': token,
                'icon': icon,
                'username': username,
                'id': id,
            }
            return APIResponse(data=data)
        else:
            return APIResponse(status=1, msg='用户名或者密码错误')

    @action(methods=['get'], detail=False)
    def check_mobile(self, request, *args, **kwargs):
        """
        检测手机号码是否注册
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        mobile = request.GET.get('mobile')
        if not verify_mobile_num(mobile,flag=0):
            return APIResponse(msg='手机号不合法',status=0)

        if models.User.objects.filter(mobile=mobile):
            return APIResponse(msg='手机号码存在', status=0)
        else:
            return APIResponse(msg='手机号码没有注册', status=1)

    @action(methods=['post'], detail=False)
    def code_login(self, request, *args, **kwargs):
        """
        这个是验证码登录接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ser = serializer.LoginCodeSerializer(data=request.data, context={'request': request})
        if ser.is_valid():
            print(ser.errors)
            token = ser.context['token']
            icon = ser.context.get('icon')
            id = ser.context.get('id')
            username = ser.context.get('username')
            data = {
                'token': token,
                'icon': icon,
                'username': username,
                'id': id,
            }
            return APIResponse(msg='登录成功', data=data)
        else:
            return APIResponse(msg='手机号或者验证码错误!', status=2)


class SendSmsViewSet(ViewSet):
    throttle_classes = [SMSSimpleRateThrottle, ]

    @action(methods=['get'], detail=False)
    def send_sms_code(self, request, *args, **kwargs):
        """
        发送短信验证码
        """
        import re
        from hhapi.libs.tx_sms import generator_code, sender_sms
        from django.core.cache import cache
        from django.conf import settings

        mobile = request.GET.get('mobile')
        print(mobile)
        if mobile is None:
            return APIResponse(status=1, msg='手机号码不能为空')
        if not re.match('^1[3-9][0-9]{9}', mobile):
            return APIResponse(status=1, msg='手机号不合法')
        code = generator_code()
        result = sender_sms(mobile, code)
        cache.set(settings.TELEPHONE_CACHE_KEY % mobile, code, settings.CACHE_TIME)
        if result:
            return APIResponse(status=0, msg='短信验证码发送成功')
        return APIResponse(status=1, msg='验证码发送失败')


class RegisterGenericViewSet(GenericViewSet, mixins.CreateModelMixin):
    """
    注册账号
    """
    queryset = models.User.objects.all()
    serializer_class = serializer.RegisterModelSerializer

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return APIResponse(msg='注册成功', username=ser.data["username"])
        else:
            # return APIResponse(msg='注册失败', status=1)
            return APIResponse(msg=ser.errors, status=1)
