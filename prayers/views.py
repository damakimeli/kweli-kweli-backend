from rest_framework import generics
from .models import PrayerRequest
from .serializers import PrayerRequestSerializer


class PrayerRequestCreateView(generics.CreateAPIView):
    """POST /api/prayers/ — submit a prayer request"""
    queryset = PrayerRequest.objects.all()
    serializer_class = PrayerRequestSerializer