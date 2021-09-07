from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .serializers import sentimentAnalysisSerializer
from .utils import remove_punct, process_data_SA, load_word_index, bundle_request_data

import numpy as np
import requests

# Create your views here.
class SentimentAnalysisView(views.APIView):
    serializer_class = sentimentAnalysisSerializer
    word_index = load_word_index("assets/word_index.json") #make sure it has correct word counts

    # get model status
    def get(self, request):
        # call tf serving
        error = False
        url = settings.SERVING_URL + "SA_model"

        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError as e:
            return Response({'error': str(e)},status.HTTP_400_BAD_REQUEST)
        
        try:
            model_status = response.json().get('model_version_status')
        except IndexError as e:
            return Response({'error': str(e)},status.HTTP_400_BAD_REQUEST)

        return Response({'response':model_status}, status=status.HTTP_200_OK)

    # use model to predict
    def post(self, request):        
        input_string = request.data.get("input_string", None)

        # validate input data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # process input data
        processed_data = process_data_SA(serializer.data, self.word_index)

        # call tf serving
        error = False
        url = settings.SERVING_URL + "SA_model:predict"
        headers = {"content-type": "application/json"}
        request_data = bundle_request_data(processed_data)

        try:
            response = requests.post(url, data=request_data, headers=headers)
        except requests.exceptions.ConnectionError as e:
            return Response({'error': str(e)},status.HTTP_400_BAD_REQUEST)

        try:
            prediction = response.json().get('predictions')[0][0]
        except IndexError as e:
            return Response({'error': str(e)},status.HTTP_400_BAD_REQUEST)

        return Response({'response':{
            'prediction': prediction
            }}, status=status.HTTP_200_OK)