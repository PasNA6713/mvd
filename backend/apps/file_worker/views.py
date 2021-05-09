import json

from django.http import HttpResponse
from wsgiref.util import FileWrapper

from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response

from apps.map.views import MapItemListView
from apps.clasterization.views import GetClastersView
from .serv import get_file, get_cluster_file
from .serializers import ImgSerializer
from .models import ImgModel, FormatedImgModel
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        detect_rect(serializer.data['id'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ImgRetrieveView(generics.RetrieveAPIView):
    serializer_class = ImgSerializer
    queryset = ImgModel.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        with open(instance.file.path, 'rb') as short_report:
            return HttpResponse(FileWrapper(short_report), content_type=f'application/pdf')


class FormatedImgRetrieveView(ImgRetrieveView):
    queryset = FormatedImgModel.objects.all()