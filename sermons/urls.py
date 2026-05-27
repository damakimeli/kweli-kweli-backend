"""
SERMONS — urls.py
"""

from django.urls import path
from .views import SermonListView, SermonDetailView

urlpatterns = [
    path('', SermonListView.as_view(), name='sermon-list'),
    path('<int:pk>/', SermonDetailView.as_view(), name='sermon-detail'),
]