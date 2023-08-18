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

from rest_framework.permissions import IsAuthenticated

# Create your views here.
# Import all models.
from .models import *
from .serializers import TranscriptSerializer
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

@login_required
def principal(request):
    user = request.user
    user_folders = Folder.objects.filter(user=user)
    return render(request, 'principal.html', {'user_folders': principal})

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
    return render(request, 'create_folder.html', {'form': form})

@login_required
def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    return render(request, 'folder_detail.html', {'folder': folder})

@login_required
def contact_view(request):
    # ... tu lógica para mostrar el perfil del usuario ...
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
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        uploaded_file_instance = UploadedFile(file=myfile)
        uploaded_file_instance.save()

        uploaded_file_url = uploaded_file_instance.file.url
        return render(request, 'upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'upload.html')

class TranscriptListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = tTranscript.objects.all()
    serializer_class = TranscriptSerializer

class TranscriptRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = tTranscript.objects.all()
    serializer_class = TranscriptSerializer



