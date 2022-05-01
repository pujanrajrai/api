from rest_framework import serializers
from .models import PictureDesc


class PictureDescSerializers(serializers.ModelSerializer):
    class Meta:
        model = PictureDesc
        fields = ['name', 'photo']
