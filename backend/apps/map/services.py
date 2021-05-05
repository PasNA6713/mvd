import json
import random
from datetime import datetime

import pandas as pd

from .models import MapItem
from .serializers import MapItemDetailSerializer


def get_random_date(start_year: int, end_year: int, hour=0, minute=0) -> datetime:
    try:
        return datetime(year=random.choice(range(start_year, end_year)),\
            month=random.choice(range(1,13)), day=random.choice(range(1, 31)),\
            hour=hour, minute=minute)
    except ValueError:
        return get_random_date(start_year, end_year, hour, minute)


def construct_datetime(date:str, time:str) -> datetime:
    day, month, year = [int(i) for i in date.split('.')]
    hour, minute, sec = [int(i) for i in time.split(':')]
    return datetime(day=day, month=month, year = year, hour=hour, minute=minute, second=sec)


def fill_db_from_csv(filename) -> None:
    df = pd.read_csv(filename)

    objs = []
    for index, row in df.iterrows():
        try:
            m = MapItem(
                category = row['Способ совершения преступления'],
                parent_region = row['n_p'],
                region = row['District'],
                address = row['street'],

                lat = row['latitude'],
                long = row['longitude'],
                
                light = row['osv'],
                datetime = construct_datetime(row['Дата совершения преступления'], row['Time']),
                organization = row['Наименование органа'],
                criminal_type=row['Вид уголовного преследования'],
                employee=row['Кем выявлено'],
                is_operative=bool(row['Выявлено по оперативным данным']),
                crime_qualification=int(row['Квалификация преступления']),
                yk_qualification=row['пункт Квалификация преступления по УК РФ'],
                severity=int(row['Тяжесть']),
                is_attempt=row['Приготовление/покушение'],
                damage=row['Ущерб'],
                crime_direction=row['Направленность'],
                money=row['Изъята-сумма'],
                drug_name=row['Наименование наркотика'],
                drug_weight=row['Изъято наркотиков - вес (грамм)'],
                victim_number=row['Число потерпевших'],
                dead_num=row['Число погибших'],
            )
        except ValueError: pass
        except AttributeError: pass
        else: objs.append(m)
    MapItem.objects.bulk_create(objs)


# if MapItem.objects.all().count() == 0:
#     fill_db_from_csv('final_mvd.csv')