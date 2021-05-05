from .models import MapItem

FIELDS_SET = {
    i.name: set(MapItem.objects.all().values_list(i.name, flat=True).distinct())
    for i in MapItem._meta.fields
}
FIELDS_SET['fields'] = {i.name for i in MapItem._meta.fields}

