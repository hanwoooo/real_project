from rest_framework import serializers
from .models import Subway

class SubwaySerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'title',
      'location',
    )
    model = Subway