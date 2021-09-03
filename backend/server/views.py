from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .serializers import sentimentAnalysisSerializer
from .utils import remove_punct, process_data_SA, load_word_index

import numpy as np

# Create your views here.
class SentimentAnalysisView(views.APIView):
    serializer_class = sentimentAnalysisSerializer
    word_index = load_word_index("assets/word_index.json") #make sure it has correct word counts

    def get(self, request):
        return Response({'request':'a'}, status=status.HTTP_200_OK)

    def post(self, request):
        input_string = request.data.get("input_string", None)

        # validate input data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # process input data
        processed_data = process_data_SA(serializer.data, self.word_index)
        print("processed_data shape: ", processed_data.shape)

        # call tf serving

        return Response({'request':processed_data}, status=status.HTTP_200_OK)