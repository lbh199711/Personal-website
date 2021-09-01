from rest_framework import serializers

class sentimentAnalysisSerializer(serializers.Serializer):
    data = serializers.CharField(max_length=4096)