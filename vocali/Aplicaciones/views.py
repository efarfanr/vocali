from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db import connection
from django.http import JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UploadFileForm, FolderForm
from .models import UploadedFile
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

from django.views.generic import ListView, CreateView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# Import all models.
from .models import *
# Import all serializers.
from .serializers import *
# Importa locale y establece la configuración regional
import locale
import json

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirige a la página de perfil después de iniciar sesión correctamente
        else:
            # Autenticación fallida, vuelve a mostrar la página de inicio de sesión con un error
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        # Solicitud GET, muestra la página de inicio de sesión
        return render(request, 'login.html')

# TEMPLATE_DIRS = (
#     'os.path.joins(BASE_DIR, "templates")'
#     )



def index(request):
    return render(request, "index.html")

@login_required
def usersprofile(request):
    return render(request, "usersprofile.html")

@login_required
def pagesfaq(request):
    return render(request, "pagesfaq.html")

@login_required
def pagescontact(request):
    return render(request, "pagescontact.html")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def wizard(request):
    return render(request, "wizard.html")

# @login_required
# def principal(request):
#     user = request.user
#     top_level_folders = Folder.objects.filter(user=user, parent_folder=None)
#     return render(request, 'principal.html', {'top_level_folders': top_level_folders})

@login_required
def principal(request):
    user = request.user
    top_level_folders = Folder.objects.filter(user=user, parent_folder=None)
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user
            folder.save()
            # Si deseas que el usuario vea un mensaje después de guardar, puedes usar los mensajes de Django.
            messages.success(request, 'Folder creado exitosamente!')
            return redirect('principal')
    else:
        form = FolderForm()
    return render(request, 'principal.html', {'form': form, 'top_level_folders': top_level_folders})


def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user
            folder.save()
            return redirect('principal')
    else:
        form = FolderForm()
    return render(request, 'principal.html', {'form': form})

@login_required
def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    return render(request, 'folder_detail.html', {'folder': folder})

@login_required
def contact_view(request):
    
    return render(request, 'contact.html')


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    try:
        usr_company = Usr_company.objects.get(user=user)
        company_name = usr_company.company_id.company_name
    except Usr_company.DoesNotExist:
        company_name = ""
    context = {
        'company_name': company_name
    }
    return render(request, 'usersprofile.html', context)


@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES['audio_video_file']:
        myfile = request.FILES['audio_video_file']

        uploaded_file_instance = UploadedFile(file=myfile)
        uploaded_file_instance.save()

        uploaded_file_url = uploaded_file_instance.file.url
        return render(request, 'upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'upload.html')

@login_required
def tType_identity_view(request):
    type_identities = tType_identity.objects.all()
    return render(request, 'type_identity.html', {'type_identities': type_identities})

@login_required
def tLanguage_view(request):
    languages = tLanguage.objects.all()
    return render(request, 'language.html', {'languages': languages})

@login_required
def company_view(request):
    companies = Company.objects.all()
    return render(request, 'company.html', {'companies': companies})

@login_required
def usr_company_view(request):
    usr_companies = Usr_company.objects.all()
    return render(request, 'usr_company.html', {'usr_companies': usr_companies})

@login_required
def folder_view(request):
    folders = Folder.objects.all()
    return render(request, 'folder.html', {'folders': folders})

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
    queryset = tSpeaker_trans.objects.all()
    serializer_class = tSpeaker_transSerializer


