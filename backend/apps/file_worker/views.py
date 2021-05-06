import json

from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from loguru import logger

from apps.map.views import MapItemListView
from apps.clasterization.views import GetClastersView
from .serv import get_file, get_cluster_file
from .serializers import ImgSerializer
from .models import ImgModel
from .image_worker.file_pdf import *


class GetMapItemsFileView(MapItemListView):
    def list(self, request, file_format):
        queryset = self.filter_queryset(self.get_queryset())
        return get_file(file_format, queryset)

class GetClusterFileView(GetClastersView):
    def list(self, request, number, file_format):
        queryset = self.filter_queryset(self.get_queryset())
        return get_cluster_file(number, file_format, queryset)

class UploadImg(generics.CreateAPIView):
    serializer_class = ImgSerializer

    @logger.catch
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return detect_rect(serializer.data['id'])
