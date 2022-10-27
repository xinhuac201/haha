from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from ..response import APIResponse


class APIListModelMixin(ListModelMixin):
    """
    list封装
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return APIResponse(data=serializer.data)


class APIRetrieveModelMixin(RetrieveModelMixin):
    """
    retrieve封装
    """
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return APIResponse(data=serializer.data)
