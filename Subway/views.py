from django.shortcuts import render
from rest_framework import generics

from .models import Subway
from .serailizers import SubwaySerializer
# Create your views here.

class ListSubway(generics.ListCreateAPIView):
  queryset = Subway.objects.all()
  serializer_class = SubwaySerializer

class DetailSubway(generics.RetrieveUpdateDestroyAPIView):
  queryset = Subway.objects.all()
  serializer_class = SubwaySerializer