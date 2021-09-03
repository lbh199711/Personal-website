from rest_framework import serializers

class sentimentAnalysisSerializer(serializers.Serializer):
    input_string = serializers.CharField(max_length=8192)