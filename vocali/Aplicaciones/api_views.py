from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import connection
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UploadFileForm, FolderForm, tType_identityForm, tLanguageForm, tTranscript, tPerson, tSpeakers_trans
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework import generics, viewsets

# API REST
class BaseListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

class BaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class Usr_companyViewSet(viewsets.ModelViewSet):
    queryset = Usr_company.objects.all()
    serializer_class = Usr_companySerializer

class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class tJson_transViewSet(viewsets.ModelViewSet):
    queryset = tEtapas_trans.objects.all()
    serializer_class = tEtapas_transSerializer





class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer




class FolderListCreateView(generics.ListCreateAPIView): 
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class FolderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

#Tipos de identidad

class tType_identityViewSet(viewsets.ModelViewSet):
    queryset = tType_identity.objects.all()
    serializer_class = tType_identitySerializer

class tType_identityListCreateView(generics.ListCreateAPIView):
    queryset = tType_identity.objects.all()
    serializer_class = tType_identitySerializer

class tType_identityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tType_identity.objects.all()
    serializer_class = tType_identitySerializer

#Lenguajes

class tLanguageViewSet(viewsets.ModelViewSet):
    queryset = tLanguage.objects.all()
    serializer_class = tLanguageSerializer

class tLanguageListCreateView(generics.ListCreateAPIView):
    queryset = tLanguage.objects.all()
    serializer_class = tLanguageSerializer

class tLanguageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tLanguage.objects.all()
    serializer_class = tLanguageSerializer

#Roles de transcripcion

class tRoles_transViewSet(viewsets.ModelViewSet):
    queryset = tRoles_trans.objects.all()
    serializer_class = tRoles_transSerializer

class tRoles_transListCreateView(generics.ListCreateAPIView):
    queryset = tRoles_trans.objects.all()
    serializer_class = tRoles_transSerializer

class tRoles_transRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tRoles_trans.objects.all()
    serializer_class = tRoles_transSerializer

#Etapas de transcripcion

class tEtapas_transViewSet(viewsets.ModelViewSet):
    queryset = tRoles_trans.objects.all()
    serializer_class = tRoles_transSerializer

class tEtapas_transListCreateView(generics.ListCreateAPIView):
    queryset = tRoles_trans.objects.all()
    serializer_class = tRoles_transSerializer

class tEtapas_transRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tRoles_trans.objects.all()
    serializer_class = tRoles_transSerializer

#Transcripciones

class tTranscriptViewSet(viewsets.ModelViewSet):
    queryset = tTranscript.objects.all()
    serializer_class = tTranscriptSerializer

class tTranscriptListCreateView(generics.ListCreateAPIView):
    queryset = tTranscript.objects.all()
    serializer_class = tTranscriptSerializer

class tTranscriptRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tTranscript.objects.all()
    serializer_class = tTranscriptSerializer

#Personas

class tPersonViewSet(viewsets.ModelViewSet):
    queryset = tPerson.objects.all()
    serializer_class = tPersonSerializer

class tPersonListCreateView(generics.ListCreateAPIView):
    queryset = tPerson.objects.all()
    serializer_class = tPersonSerializer

class tPersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tPerson.objects.all()
    serializer_class = tPersonSerializer


#Speakers

class tSpeaker_transViewSet(viewsets.ModelViewSet):
    queryset = tSpeakers_trans.objects.all()
    serializer_class = tSpeaker_transSerializer


class tSpeaker_transListCreateView(generics.ListCreateAPIView):
    queryset = tSpeakers_trans.objects.all()
    serializer_class = tSpeaker_transSerializer 

class tSpeaker_transRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tSpeakers_trans.objects.all()
    serializer_class = tSpeaker_transSerializer
