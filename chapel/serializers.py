from rest_framework import serializers
from .models import ChapelVideo


class ChapelVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapelVideo
        fields = ['id', 'title', 'speaker', 'date', 'description', 'fb_url', 'thumbnail', 'is_published']