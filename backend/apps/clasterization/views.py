from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response

from apps.map.models import MapItem
from apps.map.filters import MapItemFilter

from .clasterization import dynamic_patrol_func


class GetClastersView(generics.ListAPIView):
    queryset = MapItem.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MapItemFilter

    def list(self, request, number, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        r = dynamic_patrol_func(number, queryset)
        return Response(r, status=200)
