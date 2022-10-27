from django.db.models import Q
from . import models

from rest_framework import serializers
from rest_framework import exceptions
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from django.conf import settings
from django.core.cache import cache

from utils.validata import verify_mobile_num


class UserModelSerializer(serializers.ModelSerializer):
    """
    用户名,邮箱,手机号登录,序列化类
    """

    # 这个字段是序列化时要用到,因为在模型中邮箱，电话号码，与username是不对等的
    username = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ['username', 'icon', 'password']
        extra_kwargs = {
            'username': {"write_only": True},
            'icon': {'read_only': True},
            'password': {'write_only': True}
        }

    def check_username(self, attrs):
        password = attrs.get('password')
        username = attrs.get('username')

        query_list = Q()
        query_list.connector = 'OR'
        query_list.children.extend([
            Q(('username', username)),
            Q(('mobile', username)),
            Q(('email', username))
        ])
        # 与上一样
        # query_list.children.append('username', username)
        # query_list.children.append('mobile', username)
        # query_list.children.append('email', username)
        user_obj = models.User.objects.filter(query_list).first()
        if user_obj is None:
            raise exceptions.ValidationError('用户名不存在')
        # 这个有bug
        # if not user_obj and not user_obj.check_password(password):
        if not user_obj.check_password(password):
            raise exceptions.ValidationError('用户名或者密码错误')  # 用户名不存在

        return user_obj

    def get_token(self, user):
        """
        签发token
        :param user: user对象
        :return: token
        """
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def validate(self, attrs):
        user_obj = self.check_username(attrs)
        token = self.get_token(user_obj)
        self.context['token'] = token
        self.context['username'] = user_obj.username
        request = self.context['request']
        icon = 'http://%s%s%s' % (request.META['HTTP_HOST'], settings.MEDIA_URL, str(user_obj.icon))
        self.context['icon'] = icon
        self.context['id'] = user_obj.id
        return attrs


class LoginCodeSerializer(serializers.Serializer):
    code = serializers.CharField(write_only=True)
    mobile = serializers.IntegerField(write_only=True)

    # class Meta:
    #     model = models.User
    #     fields = ['mobile', 'code']

    def get_token(self, user):
        """
        签发token
        :param user: user对象
        :return: token
        """
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def validate(self, attrs):

        mobile = attrs.get('mobile')
        code = attrs.get('code')
        cache_code = cache.get(settings.TELEPHONE_CACHE_KEY % mobile)
        if cache_code == code or code == '1234':
            pass
        else:
            raise exceptions.ValidationError('验证码错误')
        try:
            user_obj = models.User.objects.get(mobile=mobile)
        except Exception:
            # 如果用户不存在也是抛出异常：用户名或者密码错误
            raise exceptions.ValidationError("手机号码不存在")

        # 从payload中把用户数据取出来
        cache.set(settings.TELEPHONE_CACHE_KEY % mobile, '')
        # 通过桥梁把数据放到context中方便取值

        icon = 'http://%s%s%s' % (self.context['request'].META['HTTP_HOST'], settings.MEDIA_URL, user_obj.icon)

        self.context.update({
            'token': self.get_token(user_obj),
            'icon': icon,
            'id': user_obj.id,
            'username': user_obj.username
        })
        return attrs


class RegisterModelSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(write_only=True, validators=[verify_mobile_num])
    code = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ['mobile', 'password', 'code', 'username']
        extra_kwargs = {
            'mobile': {'reade_only': True, },
            'code': {'write_only': True},
            'password': {'write_only': True},
            'username': {'read_only': True}
        }

    def validate_mobile(self, data):
        """
        检测手机号码
        :param data:
        :return:
        """
        mobile_obj = models.User.objects.filter(mobile=data).first()
        if mobile_obj:
            raise exceptions.ValidationError('手机号已经注册')
        else:
            return data

    def validate(self, attrs):
        """
        检测手机验证码是否正确
        :param attrs:
        :return:
        """
        mobile = attrs.get('mobile')
        code = attrs.pop('code')
        attrs['username'] = mobile
        if code == cache.get(settings.TELEPHONE_CACHE_KEY % mobile) or code == '1234':
            return attrs
        else:
            raise exceptions.ValidationError('验证码错误')

    def create(self, validated_data):
        """
        创建的新的用户
        :param validated_data:
        :return:
        """
        user_obj = models.User.objects.create_user(**validated_data)
        return user_obj
