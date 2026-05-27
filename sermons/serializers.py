"""
SERMONS — serializers.py
Converts Sermon database objects into JSON
so the frontend can read them.
"""

from rest_framework import serializers
from .models import Sermon


class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = [
            'id',
            'title',
            'speaker',
            'date',
            'series',
            'description',
            'fb_url',
            'thumbnail',
            'is_published',
        ]