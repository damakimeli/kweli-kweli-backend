from django.urls import path
from .views import ChapelListView, ChapelDetailView

urlpatterns = [
    path('', ChapelListView.as_view(), name='chapel-list'),
    path('<int:pk>/', ChapelDetailView.as_view(), name='chapel-detail'),
]