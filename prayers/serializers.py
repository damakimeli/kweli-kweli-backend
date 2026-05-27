from rest_framework import serializers
from .models import PrayerRequest


class PrayerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerRequest
        fields = ['id', 'name', 'email', 'request', 'submitted_at']
        read_only_fields = ['submitted_at']