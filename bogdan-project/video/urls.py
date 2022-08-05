from django.urls import path

from .views import VideoAPIView

urlpatterns = [
    path('video/', VideoAPIView.as_view())
]