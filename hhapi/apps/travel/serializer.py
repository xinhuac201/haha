from rest_framework import serializers
from . import models


class TravelBannerModelSerializer(serializers.ModelSerializer):
    """
    热门轮播图,后期这个序列化类,
    """

    class Meta:
        model = models.Banner
        fields = ['title', 'link', 'desc', 'img']


class TravelRouteDesc(serializers.ModelSerializer):
    destination = serializers.CharField(source="destination.name",read_only=True)

    class Meta:
        model = models.Route
        fields = [
            "title",
            "heading",
            "destination",
            "overview_list",
            "desc",
            "cover",
            "map",
            "duration",
            "price",

        ]
        # extra_kwargs ={'destination':{'write_only':True}}


class TravelSRouteDesc(serializers.ModelSerializer):

    class Meta:
        model = models.Route
        fields = [
            "heading",
            "cover",
            "duration",
            "price",
            "strength",
            "focus_tag_list"
        ]
