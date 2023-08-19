from rest_framework import serializers
from .models import tTranscript,tEtapas_trans

class EtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tEtapas_trans
        fields = '__all__'

class TranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = tTranscript
        fields = '__all__'
