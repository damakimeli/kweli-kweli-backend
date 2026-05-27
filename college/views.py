from rest_framework import generics
from .models import Course, Application
from .serializers import CourseSerializer, ApplicationSerializer


class CourseListView(generics.ListAPIView):
    """GET /api/college/courses/ — all active courses"""
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CourseSerializer


class ApplicationCreateView(generics.CreateAPIView):
    """POST /api/college/apply/ — submit a new application"""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer