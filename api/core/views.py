from django.shortcuts import render
from rest_framework import viewsets
from .models import Airport
from .models import Airline
from .models import Runway
from .models import Flight
from .serializers import AirportSerializer
from .serializers import AirlineSerializer
from .serializers import RunwaySerializer
from .serializers import FlightSerializer

# Create your views here.

class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

class RunwayViewSet(viewsets.ModelViewSet):
    queryset = Runway.objects.all()
    serializer_class = RunwaySerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
