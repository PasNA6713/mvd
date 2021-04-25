from .models import MapItem


LIGHT = []
CATEGORY = []
REGION = []

try:
    Items = MapItem.objects.all()
    for item in Items:
        LIGHT.append(item.light)
        REGION.append(item.region)
        CATEGORY.append(item.category)

        LIGHT = list(set(LIGHT))
        REGION = list(set(REGION))
        CATEGORY = list(set(CATEGORY))
except Exception:
    pass

    