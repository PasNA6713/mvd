import json
import os

from django.http import HttpResponse
from wsgiref.util import FileWrapper

import pandas as pd

from apps.clasterization.clasterization import dynamic_patrol_func
from apps.map.serializers import MapItemDetailSerializer
from apps.map.filters import get_items_by_ids
from apps.map.models import MapItem


def construct_data(params) -> list:
    params = list(params)
    new_params = []
    for cluster in params:
        cluster = dict(cluster)
        detail_point =  MapItemDetailSerializer(get_items_by_ids(cluster.pop('points')), many=True).data
        cluster['points'] = [dict(i) for i in detail_point]
        new_params.append(cluster)
    return new_params

def get_model_fields() -> list:
    return [i.name for i in MapItem._meta.fields][1:] + ['claster', 'claster_lat', 'claster_long']

def construct_dataframe(params: list) -> pd.DataFrame:
    data = construct_data(params)
    d = []
    for claster in range(len(data)):
        for point in data[claster].get('points'):
            string = list(point.values())[1:] + [claster, data[claster].get('lat'), data[claster].get('long')]
            d.append(string)
    col = get_model_fields()
    return pd.DataFrame(data=d, columns=col)

def create_json_file(filename: str, params: list) -> None:
    with open(filename, 'w') as outfile:
        json.dump({
            'clasters': construct_data(params)
        }, outfile, indent=4, ensure_ascii=False)

def create_csv_file(filename: str, params: list) -> None:
    construct_dataframe(params).to_csv(filename, encoding='cp1251')

def create_xlsx_file(filename: str, params: list) -> None:
    construct_dataframe(params).to_excel(filename)

def create_cluster_file(filename: str, file_format: str, params: list):
    if file_format == 'json':
        create_json_file(filename, params)
    if file_format == 'csv':
        create_csv_file(filename, params)
    if file_format == 'xlsx':
        create_xlsx_file(filename, params)