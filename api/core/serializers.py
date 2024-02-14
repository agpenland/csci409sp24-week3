from rest_framework import serializers
from core.models import Airline, Airport, Runway, Flight

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['name', 'airline_code']
        