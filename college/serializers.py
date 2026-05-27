from rest_framework import serializers
from .models import Course, Application


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'year', 'description', 'is_active']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'full_name', 'email', 'phone', 'programme', 'motivation', 'submitted_at']
        read_only_fields = ['submitted_at']