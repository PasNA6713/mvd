from django_filters import rest_framework as filters
from django.db.models import F

from .models import NewsModel


class NewsFilter(filters.FilterSet):
    posted = filters.IsoDateTimeFromToRangeFilter()

    loc = filters.CharFilter(method='filter_array')
    per = filters.CharFilter(method='filter_array')
    org = filters.CharFilter(method='filter_array')
    source = filters.CharFilter(method='get_source')

    def get_source(self, queryset, name, value):
        return queryset.filter(link__contains=value)

    def filter_array(self, queryset, name, value):
        tags_to_find = value.split(',')
        return queryset.filter(**{f'{name}__contains': tags_to_find})

    class Meta:
        model = NewsModel
        fields = ['loc', 'posted', 'org', 'per', 'source']