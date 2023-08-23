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
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from Aplicaciones.models import *
from Aplicaciones.forms import UploadFileForm, FolderForm, tType_identityForm, tLanguageForm, tRoles_transForm, tEtapas_transForm,tTranscriptForm, tPersonForm


from django.views import View
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# Import all models.
from .models import *
# Import all serializers.
from .serializers import *
# Import all API
from .api_views import *
# Import all forms.
#from .forms import *
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
def dashboard(request):
    return render(request, "dashboard.html")

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
def contact_view(request):    
    return render(request, 'contact.html')

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

@login_required
def wizard(request):
    return render(request, "wizard.html")


@login_required
def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    return render(request, 'folder_detail.html', {'folder': folder})


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



# CREATE FOLDERS AND SUBFOLDERS THE USER
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


#tipos de tIdentificación
def type_identity_view(request):
      type_identities = tType_identity.objects.all()
      return render(request, 'type_identity.html', {'type_identities': type_identities})

class tType_identityListView(ListView):
    models = tType_identity
    serializer_class = tType_identitySerializer
    template_name = 'type_identity.html'
    content_object_name = 'type_identities'
    success_url = '/type_identity/'

class tType_identityCreateView(CreateView):
    model = tType_identity
    form_class = tType_identityForm
    template_name = 'type_identity.html'
    success_url = '/type_identity/'

class tType_identityUpdateView(UpdateView):
    model=tType_identity
    form_class = tType_identityForm
    template_name = 'type_identity.html'
    success_url = '/type_identity/'

class tType_identityDeleteView(DeleteView):
    model = tType_identity
    success_url = '/type_identity/'

    def get(self,request, *args, **kwargs):
        return self.delete(request,*args, **kwargs)

#tipos de tLanguage

def tLanguage_view(request):
      tLanguages = tLanguage.objects.all()
      return render(request, 'tLanguage.html', {'languages': tLanguages})


class tLanguageListView(ListView):
    models = tLanguage
    serializer_class = tLanguageSerializer
    template_name = 'tLanguage.html'
    content_object_name = 'tLanguage'
    success_url = '/tLanguage/'

class tLanguageCreateView(CreateView):
    model = tLanguage
    form_class = tLanguageForm
    template_name = 'tLanguage.html'
    success_url = '/tLanguage/'

class tLanguageUpdateView(UpdateView):
    model=tLanguage
    form_class = tLanguageForm
    template_name = 'tLanguage.html'
    success_url = '/tLanguage/'

class tLanguageDeleteView(DeleteView):
    model = tLanguage
    success_url = '/tLanguage/'
    
    def get(self,request, *args, **kwargs):
        return self.delete(request,*args, **kwargs)

#Roles de transcripcion

def tRoles_trans_view(request):
    tRoles_transs = tRoles_trans.objects.all()
    return render(request, 'tRoles_trans.html',{'roles_trans': tRoles_transs})

class tRoles_transListView(ListView):
    models = tRoles_trans
    serializer_class = tRoles_transSerializer
    template_name = 'tRoles_trans.html'
    content_object_name = 'tRoles_trans'
    success_url = '/tRoles_trans/'

class tRoles_transCreateView(CreateView):
    models = tRoles_trans
    form_class = tRoles_transForm
    template_name = 'tRoles_trans.html'
    success_url = '/tRoles_trans/'

class tRoles_transUpdateView(UpdateView):
    model=tRoles_trans
    form_class = tRoles_transForm
    template_name = 'tRoles_trans.html'
    success_url = '/tRoles_trans/'

class tRoles_transDeleteView(DeleteView):
    model=tRoles_trans
    success_url = '/tRoles_trans/'
    def get(self,request, *args, **kwargs):
        return self.delete(request,*args, **kwargs)

#Etapas de transcripcion

def tEtapas_trans_view(request):
    tEtapas_transs = tEtapas_trans.objects.all()
    return render(request,'tEtapas_trans.html',{'etapas_trans': tEtapas_transs})

class tEtapas_transListView(ListView):
    model = tEtapas_trans
    template_name = 'tEtapas_trans.html'
    context_object_name = 'tEtapas_trans'
    success_url = '/tEtapas_trans/'

class tEtapas_transCreateView(CreateView):
    model = tEtapas_trans
    form_class = tEtapas_transForm
    template_name = 'tEtapas_trans.html'
    success_url = '/tEtapas_trans/'

class tEtapas_transUpdateView(UpdateView):
    model = tEtapas_trans
    form_class = tEtapas_transForm
    template_name = 'tEtapas_trans.html'
    success_url = '/tEtapas_trans/'

class tEtapas_transDeleteView(DeleteView):
    model = tEtapas_trans
    success_url = '/tEtapas_trans/'
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

#Transcripciones

#UPLOAD FILES MEDIA /MEDIA/UPLOAD/
@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES['audio_video_file']:
        myfile = request.FILES['audio_video_file']

        uploaded_file_instance = UploadedFile(file=myfile)
        uploaded_file_instance.save()

        uploaded_file_url = uploaded_file_instance.file.url
        return render(request, 'upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'upload.html')

def tTranscript_view(request):
    tTranscripts = tTranscript.objects.all()
    return render(request, 'tTranscript.html',{'transcripts': tTranscripts})

class tTranscriptListView(ListView):
    model = tTranscript
    template_name = 'tTranscript.html'
    context_object_name = 'tTranscript'
    success_url = '/tTranscript/'

class tTranscriptCreateView(CreateView):
    model = tTranscript
    form_class = tTranscriptForm
    template_name = 'tTranscript.html'
    success_url = '/tTranscript/'

class tTranscriptUpdateView(UpdateView):
    model = tTranscript
    form_class = tTranscriptForm
    template_name = 'tTranscript.html'
    success_url = '/tTranscript/'

class tTranscriptDeleteView(DeleteView):
    model = tTranscript
    success_url = '/tTranscript/'
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

#Personas

def tPerson_view(request):
    tPersons = tPerson.objects.all()
    return render(request, 'tPerson.html',{'persons': tPersons})

class tPersonListView(ListView):
    model = tPerson
    template_name = 'tPerson.html'
    context_object_name = 'tPerson'
    success_url = '/tPerson/'

class tPersonCreateView(CreateView):
    model = tPerson
    form_class = tPersonForm
    template_name = 'tPerson.html'
    success_url = '/tPerson/'

class tPersonUpdateView(UpdateView):
    model = tPerson
    form_class = tPersonForm
    template_name = 'tPerson.html'
    success_url = '/tPerson/'

class tPersonDeleteView(DeleteView):
    model = tPerson
    success_url = '/tPerson/'
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

