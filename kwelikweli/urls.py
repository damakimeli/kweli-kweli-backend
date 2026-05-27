"""
KWELI KWELI MINISTRIES — Main URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # API routes
    path('api/sermons/', include('sermons.urls')),
    path('api/chapel/', include('chapel.urls')),
    path('api/college/', include('college.urls')),
    path('api/prayers/', include('prayers.urls')),
]

# Serve media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)