from rest_framework import serializers
from .models import Sermon


class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = [
            'id', 'title', 'speaker', 'date', 'series',
            'description', 'fb_url', 'youtube_id',
            'thumbnail', 'is_published',
        ]