from collections import Counter

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MapItem
from .serializers import (
    MapItemDetailSerializer, MapItemCreateSerializer, MapItemPointSerializer,
    DiagramPlotSerializer, BarPlotSerializer, SomeSerializer
)
from .filters import (
    MapItemFilter,
    get_months_plot, get_column_sum_plot,
    get_items_by_ids, filter_range
)
from . import params


class MapItemCreateView(generics.CreateAPIView):
    serializer_class = MapItemCreateSerializer


class MapItemDestroyView(generics.DestroyAPIView):
    queryset = MapItem.objects.all()
    serializer_class = MapItemPointSerializer


class MapItemRetrieveView(generics.RetrieveAPIView):
    queryset = MapItem.objects.all()
    serializer_class = MapItemDetailSerializer


class MapItemListView(generics.ListAPIView):
    queryset = MapItem.objects.all()
    serializer_class = MapItemPointSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MapItemFilter


class DiagramPlotView(generics.ListAPIView):
    queryset = MapItem.objects.all()
    serializer_class = DiagramPlotSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MapItemFilter

    def list(self, request, column, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = get_column_sum_plot(queryset, column)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BarPlotView(generics.ListAPIView):
    queryset = MapItem.objects.all()
    serializer_class = BarPlotSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MapItemFilter

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = get_months_plot(queryset, 'id')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class GetSomeMapItems(generics.CreateAPIView):
    queryset = MapItem.objects.all()
    serializer_class = SomeSerializer

    def post(self, request, format=None):
        ids = request.data.get('ids')
        if ids is None: return Response(
            {"Detail": "Field 'ids' is required"},
            status=status.HTTP_400_BAD_REQUEST
        )
        data = MapItemDetailSerializer(get_items_by_ids(ids), many=True).data
        return Response(
            data,
            status=status.HTTP_200_OK
        )


class GetFilterParams(APIView):
    def get(self, request, format=None):
        return Response({
            'light': params.LIGHT,
            'region': params.REGION,
            'category': params.CATEGORY
        })


class GetRangeMapItems(generics.ListCreateAPIView):
    queryset = MapItem.objects.all()
    serializer_class = MapItemPointSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MapItemFilter

    def post(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        all_points = [dict(i) for i in self.get_serializer(queryset, many=True).data]
        cur_point = {
            'lat': float(request.data.get('lat')),
            'long': float(request.data.get('long'))
        }
        data = filter(lambda x: filter_range(cur_point, x, 0.01), all_points)
        return Response(data, status=200)