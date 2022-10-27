from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from django.conf import settings

from utils.mixin import APIListModelMixin
from . import serializer
from . import models
from .searchFilter import TagSearchFilter

# Create your views here.


class HotBannerViewSet(GenericViewSet, APIListModelMixin):
    """
    热门景点banner图
    """
    serializer_class = serializer.HotBannerModelSerializer
    queryset = models.HotBanner.objects.filter(is_delete=False,is_show=True).order_by('order')[:settings.BANNER_SIZE]
    # queryset = models.HotBanner.objects.filter(is_delete=False,is_show=True).order_by('order')[:5]


class TagBannerViewSet(GenericViewSet,APIListModelMixin):
    serializer_class = serializer.TagBannerSerializer
    queryset = models.TagBanner.objects.filter(is_show=True,is_delete=False).order_by('order')
    filter_backends = [TagSearchFilter]


class TopBannerViewSet(GenericViewSet, APIListModelMixin):
    """
    热门景点banner图
    """
    serializer_class = serializer.TopBannerModelSerializer
    queryset = models.TopBanner.objects.filter(is_delete=False,is_show=True).order_by('order')[:settings.BANNER_SIZE]
