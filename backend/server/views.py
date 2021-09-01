from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from .serializers import sentimentAnalysisSerializer

# Create your views here.
class SentimentAnalysisView(views.APIView):
    serializer_class = sentimentAnalysisSerializer

    def get(self, request):
        return Response({'request':'a'}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({'request':'b'}, status=status.HTTP_202_ACCEPTED)