from django.contrib import admin
from .models import Course, Application


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display  = ('year', 'name', 'is_active')
    list_filter   = ('year', 'is_active')
    search_fields = ('name',)
    list_editable = ('is_active',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display  = ('submitted_at', 'full_name', 'email', 'phone', 'programme', 'status')
    list_filter   = ('status', 'programme')
    search_fields = ('full_name', 'email', 'phone')
    ordering      = ('-submitted_at',)
    list_editable = ('status',)  # change status directly from the list view

    readonly_fields = ('submitted_at',)