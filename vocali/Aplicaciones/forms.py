# forms.py
from django import forms
from .models import *

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent_folder']


class tLanguageForm(forms.ModelForm):
    class Meta:
        model = tLanguage
        fields = ['description_language','short_description_language','enable']

class tType_identityForm(forms.ModelForm):
    class Meta:
        model = tType_identity
        fields = ['name_type_identity','short_name_type_identity','enable']

class tRoles_transForm(forms.ModelForm):
    class Meta:
        model = tRoles_trans
        fields = ['rol_transcrip_name','enable']

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent_folder']
        
class tEtapas_transForm(forms.ModelForm):
    class Meta:
        model = tEtapas_trans
        fields = ['etapa_name','enable']

class tTranscriptForm(forms.ModelForm):
    id_etapa_trans = forms.ModelChoiceField(queryset=tEtapas_trans.objects.all(), required=True, label='Etapa')
    class Meta:
        model = tTranscript
        fields = ['number_proces_transcript','name_transcript','description_transcript','s3_video_url','idjson_trans','id_etapa_trans','id_folder','enable']



class tPersonForm(forms.ModelForm):
    class Meta:
        model = tPerson
        fields = ['id_type_identity','identity_person','first_name_person','last_name_person','alias_person','description_person','Id_language','enable']

class tSpeaker_transForm(forms.ModelForm):
     class Meta:
         model = tSpeakers_trans
         fields = ['name_spk_trans','id_transcript','id_person','id_roles_trans','uploaded_file','enable']








    





