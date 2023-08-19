from django.db import models
import requests
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import PermissionDenied
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField
from django.contrib.auth import get_user_model

# Create your models here.

class company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_nit = models.CharField(max_length=15,blank=True, null=True)
    company_name = models.CharField(max_length=50,blank=True, null=True)
    company_short_name = models.CharField(max_length=12,blank=True, null=True) 
    enable = models.BooleanField(default=False)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        
    def __str__(self):
        return self.company_name  # Mostrar el nombre de la empresa en lugar de "object (x)"

    
    # def __str__(self):
    #     return self.empresa_id
    
class Usr_company(models.Model):
    usr_company_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_id = models.ForeignKey(company, on_delete=models.CASCADE, null=True)
    usr_mobile = models.CharField(max_length=15,blank=True, null=True)
    enable = models.BooleanField(default=False)
    date_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Usuario Autorizado"
        verbose_name_plural = "Usuario Autorizado"
    
    def __str__(self):
        return self.company_id
    # def __str__(self):
    #     return str(self.company_nom) 

class Folder(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Carpeta"
        verbose_name_plural = "Carpetas"
        
    def __str__(self):
        return self.name

    
class tType_identity(models.Model):
    id_type_identity = models.AutoField(primary_key=True)
    name_type_identity = models.CharField(max_length=50,blank=True, null=True)
    short_name_type_identity = models.CharField(max_length=50,blank=True, null=True)
    enable = models.BooleanField(default=False)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tipo de Identidad"
        verbose_name_plural = "Tipos de Identidades"
        
    def __str__(self):
        return self.name_type_identity  

class tLanguage(models.Model):
    Id_language = models.AutoField(primary_key=True)
    description_language = models.CharField(max_length=30,blank=True, null=True)
    short_description_language = models.CharField(max_length=2,blank=True, null=True)
    enable = models.BooleanField(default=False)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Lenguaje"
        verbose_name_plural = "Lenguajes"
        
    def __str__(self):
        return self.description_language 

class tRoles_trans(models.Model):
    id_roles_trans = models.AutoField(primary_key=True)
    rol_transcrip_name = models.CharField(max_length=50,blank=True, null=True)
    enable = models.BooleanField(default=False)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        
    def __str__(self):
        return self.rol_transcrip_name 

class tEtapas_trans(models.Model):
    id_etapa_trans = models.AutoField(primary_key=True)
    etapa_name = models.CharField(max_length=50,blank=True, null=True)
    enable = models.BooleanField(default=False)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"
        
    def __str__(self):
        return self.etapa_name 

class tJson_trans(models.Model):
    idjson_trans = models.AutoField(primary_key=True)
    json_trans = JSONField(blank=True, null=True) # JSON data from the external URL
    json_url_trans = models.CharField(max_length=100, blank=True, null=True) # URL to fetch JSON data
    enable = models.BooleanField(default=False)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Json"
        verbose_name_plural = "Json's"

    def _str_(self):
        return str(self.json_trans) # Return the JSON

    def fetch_json(self):
        if self.json_url_trans:
            response = requests.get(self.json_url_trans)
            if response.status_code == 200:
                self.json_trans = response.json()
                self.save()
            else:
                response.raise_for_status()
        else:
            raise ValueError("No URL defined for this object")


class tTranscript(models.Model):
    id_transcript = models.AutoField(primary_key=True)
    number_proces_transcript = models.CharField(max_length=15,blank=True, null=True)
    name_transcript = models.CharField(max_length=60,blank=True, null=True)
    date_transcript = models.DateTimeField(auto_now=True)
    description_transcript = models.CharField(max_length=1024,blank=True, null=True)
    s3_video_url = models.CharField(max_length=100,blank=True, null=True) # url con procedimiento de disminución
    idjson_trans = models.ForeignKey(tJson_trans, on_delete=models.CASCADE, null=True) 
    id_etapa_trans = models.ForeignKey(tEtapas_trans, on_delete=models.CASCADE, null=True) 
    enable = models.BooleanField(default=False)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Transcripción"
        verbose_name_plural = "Transcripciones"
        
    def __str__(self):
        return self.name_transcript 
    

class tPerson(models.Model):
    id_person = models.AutoField(primary_key=True)
    id_type_identity = models.ForeignKey(tType_identity, on_delete=models.CASCADE, null=True)
    identity_person = models.CharField(max_length=15,blank=True, null=True)
    first_name_person = models.CharField(max_length=30,blank=True, null=True)
    last_name_person = models.CharField(max_length=30,blank=True, null=True)
    alias_person = models.CharField(max_length=60,blank=True, null=True)
    description_person = models.CharField(max_length=1024,blank=True, null=True)
    Id_language = models.ForeignKey(tLanguage, on_delete=models.CASCADE, null=True)
    enable = models.BooleanField(default=False)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        
    def __str__(self):
        return self.name_person 

# models File upload.
class UploadedFile(models.Model):
    file = models.FileField(upload_to='upload/')

# Speaker esta tabla el objetivo de asociar una persona con una transcripción y aquí se le agrega cual es el rol dentro de la transcripción
class tSpeaker_trans(models.Model): 
    id_spk_trans = models.AutoField(primary_key=True)
    name_spk_trans = models.CharField(max_length=50,blank=True, null=True)
    timestamp_spk_trans = models.DateTimeField(auto_now=True) # arreglo 
    id_transcript = models.OneToOneField(tTranscript, on_delete=models.CASCADE)
    id_person = models.OneToOneField(tPerson, on_delete=models.CASCADE)
    id_roles_trans = models.OneToOneField(tRoles_trans, on_delete=models.CASCADE)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE, null=True, blank=True, related_name="transcripts")
    enable = models.BooleanField(default=False)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Speaker"
        verbose_name_plural = "Speakers"
        
    def __str__(self):
        return self.name_spk_trans 


