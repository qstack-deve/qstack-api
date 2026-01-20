from django.urls import path
from . import views

urlpatterns = [
    path('suggestions/', views.SuggestionView.as_view(), name='suggestions'),
]
