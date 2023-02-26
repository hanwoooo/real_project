from rest_framework import serializers
from .models import Subway


class SubwaySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'X_location',
            'Y_location',
        )
        model = Subway
