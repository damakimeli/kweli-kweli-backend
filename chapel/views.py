from rest_framework import generics
from .models import ChapelVideo
from .serializers import ChapelVideoSerializer


class ChapelListView(generics.ListAPIView):
    """GET /api/chapel/ — all published chapel videos, newest first"""
    serializer_class = ChapelVideoSerializer

    def get_queryset(self):
        queryset = ChapelVideo.objects.filter(is_published=True)
        year = self.request.query_params.get('year')
        if year:
            queryset = queryset.filter(date__year=year)
        return queryset


class ChapelDetailView(generics.RetrieveAPIView):
    """GET /api/chapel/<id>/"""
    queryset = ChapelVideo.objects.filter(is_published=True)
    serializer_class = ChapelVideoSerializer