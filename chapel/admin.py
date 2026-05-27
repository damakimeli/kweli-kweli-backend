from django.contrib import admin
from .models import ChapelVideo


@admin.register(ChapelVideo)
class ChapelVideoAdmin(admin.ModelAdmin):
    list_display  = ('date', 'title', 'speaker', 'is_published')
    list_filter   = ('is_published', 'date')
    search_fields = ('title', 'speaker')
    ordering      = ('-date',)
    list_editable = ('is_published',)