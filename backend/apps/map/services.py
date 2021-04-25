import json
import random
from datetime import datetime

import pandas as pd

from .models import MapItem
from .serializers import MapItemDetailSerializer


def fill_db_from_json(file):
    data = json.load(file)['features']
    data = list(filter(lambda x: x['properties']['point']['lat'], data))
    items = []
    for i in data:
        item = i['properties']
        items.append(MapItem(
            datetime=item['datetime'], parent_region=item['parent_region'], region = item['region'],
            address=item['address'], lat=item['point']['lat'], long=item['point']['long'],
            category=item['category'], deaths =item['dead_count'], injured=item['injured_count'],
            light=item['light'], weather=item['weather'], nearby=item['nearby'],
            road_conditions=item['road_conditions']))
        logger.info(f'{items[-1]} - Created!')
    MapItem.objects.bulk_create(items)

def fill_db_from_css(filename) -> None:
    df = pd.read_csv(filename)
    objs = [
        MapItem(
            category = row['Prestuplenie'],
            parent_region = row['n_p'],
            region = row['District'],
            address = row['street'],

            lat = row['latitude'],
            long = row['longitude'],
            
            light = row['osv'],
            datetime = get_random_date(2015, 2020, *list(map(lambda x: int(x), row['Time'].split(':')))[:2])
        )
        for index, row in df.iterrows()
    ]
    MapItem.objects.bulk_create(objs)

def get_random_date(start_year: int, end_year: int, hour=0, minute=0) -> datetime:
    try:
        return datetime(year=random.choice(range(start_year, end_year)),\
            month=random.choice(range(1,13)), day=random.choice(range(1, 31)),\
            hour=hour, minute=minute)
    except ValueError:
        return get_random_date(start_year, end_year, hour, minute)

# fill_db_from_css('mvd.csv')
