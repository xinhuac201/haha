from rest_framework.filters import BaseFilterBackend


class TagSearchFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        tag = request.GET.get('tag')
        if tag:
            return queryset.filter(tag=tag)
        return queryset
