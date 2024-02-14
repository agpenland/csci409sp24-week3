from rest_framework import serializers
from core.models import Airline, Airport, Runway, Flight

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['name', 'airline_code']


class RunwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Runway
        fields = ['airport', 'runway_number', 'runway_designation', 'length', 'width']


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['origin', 'destination', 'airline', 'departure', 'arrival', 'flight_number', 'aircraft_type']