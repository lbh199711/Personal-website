from django.urls import path, include
from rest_framework import routers
from server.views import SentimentAnalysisView

urlpatterns = [
    path('sentiment-analysis', SentimentAnalysisView.as_view(), name="SentimentAnalysis")
]