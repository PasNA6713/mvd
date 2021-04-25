import os
import json

from django.http import HttpResponse
from wsgiref.util import FileWrapper

import pandas as pd
from django_pandas.io import read_frame

from apps.map.serializers import MapItemDetailSerializer
from apps.clasterization.clasterization import dynamic_patrol_func
from .services import create_cluster_file


def send_file(filename: str, file_format: str) -> HttpResponse:
    with open(filename, 'rb') as short_report:
        # конструирование ответа
        content = f'application/{file_format}'
        response = HttpResponse(
                FileWrapper(short_report),
                content_type=content
            )
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        os.remove(filename) # удаление файла
        return response

def get_file(file_format: str, queryset) -> HttpResponse:
    filename = f'data.{file_format}'
    if file_format == 'xlsx': 
        df = read_frame(queryset)
        df['datetime'] = df['datetime'].apply(lambda a: pd.to_datetime(a))
        df.to_csv(filename)
    elif file_format == 'csv': read_frame(queryset).to_csv(filename)
    elif file_format == 'json':
        with open(filename, 'w') as outfile:
            json.dump(MapItemDetailSerializer(queryset, many=True).data, outfile, indent=4, ensure_ascii=False)
    return send_file(filename, file_format)

def get_cluster_file(number: int, file_format: str, queryset) -> HttpResponse:
    filename = f'data.{file_format}'
    create_cluster_file(filename, file_format, dynamic_patrol_func(number, queryset))
    return send_file(filename, file_format)
    