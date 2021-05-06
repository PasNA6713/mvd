from rest_framework import serializers

from .models import ImgModel


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgModel
        fields = '__all__'