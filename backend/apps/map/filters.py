from django_filters import rest_framework as filters

from django.db.models.functions import TruncMonth, Cast
from django.db.models import Q, Count, F, DateField

from .models import MapItem


def get_items_by_ids(ids: list):
    q = Q()
    for i in ids:
        q |= Q(pk=i)
    return MapItem.objects.filter(q)

def filter_range(base_point, second_point, min_range: float) -> bool:
    return sqrt((base_point['lat']-second_point['lat'])**2 + (base_point['long']-second_point['long'])**2) < min_range

def get_time_group(queryset, name, number):
    if number==3:
        start_time = 21
        end_time = 2
        return queryset.filter(Q(datetime__hour__gte=start_time) | Q(datetime__hour__lt=end_time))
    elif number==0:
        start_time = 2
        end_time = 11
    elif number==1:
        start_time = 11
        end_time = 16
    elif number==2:
        start_time = 16
        end_time = 21
    return queryset.filter(Q(datetime__hour__gte=start_time) & Q(datetime__hour__lt=end_time))

def get_months_plot(queryset, field) -> list:
    return queryset.annotate(date=Cast('datetime', output_field=DateField()))\
        .values('date').annotate(month=TruncMonth('date'))\
        .values('month').annotate(c=Count(field)).values('month', 'c')\
        .order_by('month')

def get_column_sum_plot(queryset, field) -> list:
    return queryset.values(field).annotate(field=F(field), c=Count(field)).order_by('-c').values('field', 'c')


class MapItemFilter(filters.FilterSet):
    datetime = filters.IsoDateTimeFromToRangeFilter(field_name='datetime')
    time_group = filters.NumberFilter(method=get_time_group)

    class Meta:
        model = MapItem
        exclude = ['lat', 'long', 'id']