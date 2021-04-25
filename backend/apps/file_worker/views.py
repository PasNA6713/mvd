import json

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from apps.map.views import MapItemListView
from apps.clasterization.views import GetClastersView
from .serv import get_file, get_cluster_file


class GetMapItemsFileView(MapItemListView):
    def list(self, request, file_format):
        queryset = self.filter_queryset(self.get_queryset())
        return get_file(file_format, queryset)

class GetClusterFileView(GetClastersView):
    def list(self, request, number, file_format):
        queryset = self.filter_queryset(self.get_queryset())
        return get_cluster_file(number, file_format, queryset)
