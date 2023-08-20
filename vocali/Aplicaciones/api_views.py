from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UploadFileForm, FolderForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# API REST
class BaseListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

class BaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]


class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class Usr_companyListCreateView(generics.ListCreateAPIView):
    queryset = Usr_company.objects.all()
    serializer_class = Usr_companySerializer

class Usr_companyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usr_company.objects.all()
    serializer_class = Usr_companySerializer

class FolderListCreateView(generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class FolderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class tType_identityListCreateView(generics.ListCreateAPIView):
    queryset = tType_identity.objects.all()
    serializer_class = tType_identitySerializer

class tType_identityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tType_identity.objects.all()
    serializer_class = tType_identitySerializer

class tLanguageListCreateView(generics.ListCreateAPIView):
    queryset = tLanguage.objects.all()
    serializer_class = tLanguageSerializer

class tLanguageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tLanguage.objects.all()
    serializer_class = tLanguageSerializer

class tRoles_transListCreateView(generics.ListCreateAPIView):
    queryset = tRoles_trans.objects.all()
    serializer_class = tRoles_transSerializer

class tRoles_transRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tRoles_trans.objects.all()
    serializer_class = tRoles_transSerializer
    
class tEtapas_transListCreateView(generics.ListCreateAPIView):
    queryset = tEtapas_trans.objects.all()
    serializer_class = tEtapas_transSerializer

class tEtapas_transRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tEtapas_trans.objects.all()
    serializer_class = tEtapas_transSerializer

class tJson_transListCreateView(generics.ListCreateAPIView):
    queryset = tJson_trans.objects.all()
    serializer_class = tJson_transSerializer

class tjSon_transRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tJson_trans.objects.all()
    serializer_class = tJson_transSerializer

class tTranscriptListCreateView(generics.ListCreateAPIView):
    queryset = tTranscript.objects.all()
    serializer_class = tTranscriptSerializer

class tTranscriptRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tTranscript.objects.all()
    serializer_class = tTranscriptSerializer

class tPersonListCreateView(generics.ListCreateAPIView):
    queryset = tPerson.objects.all()
    serializer_class = tPersonSerializer

class tPersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tPerson.objects.all()
    serializer_class = tPersonSerializer

class UploadedFileListCreateView(generics.ListCreateAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

class UploadedFileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

class tSpeaker_transListCreateView(generics.ListCreateAPIView): 
    queryset = tSpeaker_trans.objects.all()
    serializer_class = tSpeaker_transSerializer

class tSpeaker_transRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  tSpeaker_trans.objects.all()
    serializer_class =  tSpeaker_transSerializer