from rest_framework import serializers
from .models import tTranscript

class TranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = tTranscript
        fields = '__all__'
