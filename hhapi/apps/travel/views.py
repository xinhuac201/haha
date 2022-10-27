from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from django.conf import settings

from utils.mixin import APIListModelMixin
from . import serializer
from . import models
from .searchFilter import CategorySearchFilter


# Create your views here.
class CategoryBannerViewSet(GenericViewSet, APIListModelMixin):
    serializer_class = serializer.TravelBannerModelSerializer
    queryset = models.Banner.objects.filter(is_show=True, is_delete=False).order_by('order')
    filter_backends = [CategorySearchFilter]


class TravelRouteDescViewSet(GenericViewSet, APIListModelMixin):
    serializer_class = serializer.TravelRouteDesc
    queryset = models.Route.objects.filter(status=0).order_by('routeSort')
    filter_backends = [CategorySearchFilter]


class TravelShortRouteDescViewSet(GenericViewSet, APIListModelMixin):
    serializer_class = serializer.TravelSRouteDesc
    queryset = models.Route.objects.filter(status=0,category__name="s").order_by("routeSort")
