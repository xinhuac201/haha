from rest_framework import serializers
from . import models


class HotBannerModelSerializer(serializers.ModelSerializer):
    """
    热门轮播图,后期这个序列化类,可能是通用类
    """

    class Meta:
        model = models.HotBanner
        fields = ['title', 'link', 'desc', 'img']


class TagBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TagBanner
        fields = ['title', 'link', 'desc', 'img']


class TopBannerModelSerializer(serializers.ModelSerializer):
    """
    热门轮播图,后期这个序列化类,可能是通用类
    """

    class Meta:
        model = models.TopBanner
        fields = ['title', 'link', 'desc', 'img']
