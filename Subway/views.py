from django.shortcuts import render
from rest_framework import generics

from .models import Subway
from .serailizers import SubwaySerializer

import json
# Create your views here.

class ListSubway(generics.ListCreateAPIView):
  queryset = Subway.objects.all()
  serializer_class = SubwaySerializer

class DetailSubway(generics.RetrieveUpdateDestroyAPIView):
  queryset = Subway.objects.all()
  serializer_class = SubwaySerializer

with open('./data.json', 'r') as f:
  json_data = json.load(f)
  print(json.dumps(json_data, indent="\t"))