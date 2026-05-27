from django.urls import path
from .views import PrayerRequestCreateView

urlpatterns = [
    path('', PrayerRequestCreateView.as_view(), name='prayer-request'),
]