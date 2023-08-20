from django.contrib import admin
# from django.contrib.auth.views import login, logout_the_login #29/05/2023
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django import views
from . import views, api_views 
from django.urls import path

router = DefaultRouter()


urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('contact/', views.contact_view, name='contact'),
    # ... rutas de seguridad
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('usersprofile/', views.usersprofile, name='usersprofile'),
    path('pagesfaq/', views.pagesfaq, name='pagesfaq'),
    path('pagescontact/', views.pagescontact, name='pagescontact'),
    path('principal/', views.principal, name='principal'),
    path('type_identity/', views.tType_identity_view, name='type_identity'),
    
    path('folder/<int:folder_id>/', views.folder_detail, name='folder_detail'),
    # path('create_folder/', views.create_folder, name='create_folder'),
    path('dashboard/', views.dashboard, name='dashboard'),
    

    path('upload/', views.upload_file, name='upload_file'),


    path('api/company/', views.CompanyListCreateView.as_view(), name='company-list-create'),
    path('api/company/<int:pk>/', views.CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),

    path('api/usr_company/', views.Usr_companyListCreateView.as_view(), name='usr_company-list-create'),
    path('api/usr_company/<int:pk>/', views.Usr_companyRetrieveUpdateDestroyView.as_view(), name='usr_company-detail'),

    path('api/folder/', views.FolderListCreateView.as_view(), name='folder-list-create'),
    path('api/folder/<int:pk>/', views.FolderRetrieveUpdateDestroyView.as_view(), name='folder-detail'),
    #path('api/folder/<int:folder_id>/files/', views.folder_files, name='folder_files'),
    #path('api/folder/<int:folder_id>/files/<int:file_id>/', views.folder_file_detail, name='folder_file_detail'),
    #path('api/folder/<int:folder_id>/files/<int:file_id>/transcripts/', views.folder_file_transcripts, name='folder_file_transcripts'),

    path('api/tType_identity/', views.tType_identityListCreateView.as_view(), name='tType_identity-list-create'),
    path('api/tType_identity/<int:pk>/', views.tType_identityRetrieveUpdateDestroyView.as_view(), name='tType_identity-detail'),

    path('api/tLanguage/', views.tLanguageListCreateView.as_view(), name='tLanguage-list-create'),
    path('api/tLanguage/<int:pk>/', views.tLanguageRetrieveUpdateDestroyView.as_view(), name='tLanguage-detail'),

    path('api/tRoles_trans/', views.tRoles_transListCreateView.as_view(), name='tRoles_trans-list-create'),
    path('api/tRoles_trans/<int:pk>/', views.tRoles_transRetrieveUpdateDestroyView.as_view(), name='tRoles_trans-detail'),

    path('api/tEtapas_trans/', views.tEtapas_transListCreateView.as_view(), name='tEtapas_trans-list-create'),
    path('api/tEtapas_trans/<int:pk>/', views.tEtapas_transRetrieveUpdateDestroyView.as_view(), name='tEtapas_trans-detail'),
        
    path('api/tJson_trans/', views.tJson_transListCreateView.as_view(), name='tJson_trans-list-create'), 
    path('api/tJson_trans/<int:pk>/', views.tjSon_transRetrieveUpdateDestroyView.as_view(), name='tJson_trans-detail'),

    path('api/tTranscript/', views.tTranscriptListCreateView.as_view(), name='tTranscript-list-create'),
    path('api/tTranscript/<int:pk>/', views.tTranscriptRetrieveUpdateDestroyView.as_view(), name='tTranscript-detail'),
  
    path('api/tPerson/', views.tPersonListCreateView.as_view(), name='tPerson-list-create'),
    path('api/tPerson/<int:pk>/', views.tPersonRetrieveUpdateDestroyView.as_view(), name='tPerson-detail'),

    path('api/uploaded_file/', views.UploadedFileListCreateView.as_view(), name='uploaded_file-list-create'),
    path('api/uploaded_file/<int:pk>/', views.UploadedFileRetrieveUpdateDestroyView.as_view(), name='uploaded_file-detail'),

    path('api/tSpeaker_trans/', views.tSpeaker_transListCreateView.as_view(), name='tSpeaker_trans-list-create'),
    path('api/tSpeaker_trans/<int:pk>/', views.tSpeaker_transRetrieveUpdateDestroyView.as_view(), name='tSpeaker_trans-detail'),
  
    # ... Rutas de las paginas del aplicativo
    ]

