from django.contrib import admin
# from django.contrib.auth.views import login, logout_the_login #29/05/2023
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django import views
from . import views 
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_view, name='contact'),
    # ... rutas de seguridad
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('usersprofile/', views.usersprofile, name='usersprofile'),
    path('pagesfaq/', views.pagesfaq, name='pagesfaq'),
    path('pagescontact/', views.pagescontact, name='pagescontact'),
    path('principal/', views.principal, name='principal'),
    path('folder/<int:folder_id>/', views.folder_detail, name='folder_detail'),
    # path('create_folder/', views.create_folder, name='create_folder'),
    path('dashboard/', views.dashboard, name='dashboard'),
    

    path('upload/', views.upload_file, name='upload_file'),

    path('api/transcripts/', views.TranscriptListCreateView.as_view(), name='transcript-list-create'),
    path('api/transcripts/<int:pk>/', views.TranscriptRetrieveUpdateDestroyView.as_view(), name='transcript-detail'),
    path('api/etapas/', views.EtapaListCreateView.as_view(), name='etapa-list-create'),
    path('api/etapas/<int:pk>/', views.EtapaRetrieveUpdateDestroyView.as_view(), name='etapa-detail'),

    # ... Rutas de las paginas del aplicativo
    ]

