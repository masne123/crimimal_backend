from rest_framework import serializers
from .models import User, CrimeType, Location, Report

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CrimeTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = CrimeType
        fields = '__all__'

class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
