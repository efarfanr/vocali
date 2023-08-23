from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class Usr_companySerializer(serializers.ModelSerializer):
    class Meta:
        model = Usr_company
        fields = '__all__'


class tType_identitySerializer(serializers.ModelSerializer):
    class Meta:
        model = tType_identity
        fields = '__all__'

class tLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = tLanguage
        fields = '__all__'

class tRoles_transSerializer(serializers.ModelSerializer):
    class Meta:
        model = tRoles_trans
        fields = '__all__'
 
class tJson_transSerializer(serializers.ModelSerializer):
    class Meta:
        model = tJson_trans
        fields = '__all__'


class tEtapas_transSerializer(serializers.ModelSerializer):
    class Meta:
        model = tEtapas_trans
        fields = '__all__'


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'

class tTranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = tTranscript
        fields = '__all__'

class tPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = tPerson
        fields = '__all__'


class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'

class tSpeaker_transSerializer(serializers.ModelSerializer):
    class Meta:
        model = tSpeakers_trans
        fields = '__all__'




