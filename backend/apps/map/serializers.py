from rest_framework import serializers

from .models import MapItem


class MapItemPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapItem
        fields = ['id', 'lat', 'long']

        
class MapItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapItem
        fields = '__all__'


class MapItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapItem
        fields = ['lat', 'long']


class BarPlotSerializer(serializers.Serializer):
    month = serializers.DateField()
    c = serializers.IntegerField()

class SomeSerializer(serializers.Serializer):
    ids = serializers.ListField(required=True)

class DiagramPlotSerializer(serializers.Serializer):
    field = serializers.CharField(required=False)
    c = serializers.IntegerField()
