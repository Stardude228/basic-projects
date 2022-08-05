from django.urls import path

from .views import TemplateView

urlpatterns = [
    path('temp/', TemplateView.as_view()),
]