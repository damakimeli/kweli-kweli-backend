"""
SERMONS — admin.py
This registers Sermon in the Django admin panel.
Go to http://127.0.0.1:8000/admin to add sermons
without touching any code.
"""

from django.contrib import admin
from .models import Sermon


@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display  = ('date', 'title', 'speaker', 'series', 'is_published')
    list_filter   = ('is_published', 'series', 'date')
    search_fields = ('title', 'speaker', 'series')
    ordering      = ('-date',)
    list_editable = ('is_published',)

    fieldsets = (
        ('Sermon Details', {
            'fields': ('title', 'speaker', 'date', 'series', 'description')
        }),
        ('Video & Media', {
            'fields': ('fb_url', 'youtube_id', 'thumbnail')
        }),
        ('Publishing', {
            'fields': ('is_published',)
        }),
    )