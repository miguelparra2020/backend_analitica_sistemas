from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Estadistica
from .serializers import EstadisticaSerializer

class EstadisticaListCreateView(generics.ListCreateAPIView):
    queryset = Estadistica.objects.all()
    serializer_class = EstadisticaSerializer

class EstadisticaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estadistica.objects.all()
    serializer_class = EstadisticaSerializer
