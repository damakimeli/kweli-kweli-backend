from django.contrib import admin
from .models import PrayerRequest


@admin.register(PrayerRequest)
class PrayerRequestAdmin(admin.ModelAdmin):
    list_display  = ('submitted_at', 'name', 'email', 'is_prayed_for')
    list_filter   = ('is_prayed_for',)
    search_fields = ('name', 'email')
    ordering      = ('-submitted_at',)
    list_editable = ('is_prayed_for',)  # tick it off once prayed for
    readonly_fields = ('submitted_at',)