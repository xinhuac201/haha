from rest_framework.filters import BaseFilterBackend


class CategorySearchFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        category = request.GET.get('category')
        if category:
            return queryset.filter(category__name=category)
        return queryset
