"""
SERMONS — views.py
Handles the API requests from the frontend.
"""

from rest_framework import generics
from .models import Sermon
from .serializers import SermonSerializer


class SermonListView(generics.ListAPIView):
    """
    GET /api/sermons/
    Returns all published sermons, newest first.
    Supports filtering by series: /api/sermons/?series=Walking with God
    """
    serializer_class = SermonSerializer

    def get_queryset(self):
        queryset = Sermon.objects.filter(is_published=True)
        series = self.request.query_params.get('series')
        year   = self.request.query_params.get('year')

        if series:
            queryset = queryset.filter(series__icontains=series)
        if year:
            queryset = queryset.filter(date__year=year)

        return queryset


class SermonDetailView(generics.RetrieveAPIView):
    """
    GET /api/sermons/<id>/
    Returns a single sermon by ID.
    """
    queryset = Sermon.objects.filter(is_published=True)
    serializer_class = SermonSerializer