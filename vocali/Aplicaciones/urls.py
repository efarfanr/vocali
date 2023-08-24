from django.urls import include, path
from django.contrib import admin
from rest_framework import routers


#DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

from django import views
from . import views, api_views 

router = routers.DefaultRouter()
router.register(r'company', api_views.CompanyViewSet)
router.register(r'usr_company', api_views.Usr_companyViewSet)
router.register(r'folder', api_views.FolderViewSet)
router.register(r'tType_identity', api_views.tType_identityViewSet)
router.register(r'tLanguage', api_views.tLanguageViewSet)
router.register(r'tRoles_trans', api_views.tRoles_transViewSet)
router.register(r'tEtapas_trans', api_views.tEtapas_transViewSet)
router.register(r'tJson_trans', api_views.tJson_transViewSet)
router.register(r'tTranscript', api_views.tTranscriptViewSet)
router.register(r'tPerson', api_views.tPersonViewSet)
router.register(r'uploaded_file', api_views.UploadedFileViewSet)
router.register(r'tSpeakes_trans', api_views.tSpeaker_transViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),

    path('contact/', views.contact_view, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('usersprofile/', views.usersprofile, name='usersprofile'),
    path('pagesfaq/', views.pagesfaq, name='pagesfaq'),
    path('pagescontact/', views.pagescontact, name='pagescontact'),
    path('principal/', views.principal, name='principal'),
    path('dashboard/', views.dashboard, name='dashboard'),


    path('api/folder/', views.FolderListCreateView.as_view(), name='folder-list-create'),
    path('api/folder/<int:pk>/', views.FolderRetrieveUpdateDestroyView.as_view(), name='folder-detail'),
# Tipos de identidad
    path('type_identity/', views.type_identity_view, name='type_identity'),
    path('createType_identity', views.tType_identityCreateView.as_view(),name='createType_identity'),
    path('updateType_identity/<int:pk>/', views.tType_identityUpdateView.as_view(),name='updateType_identity'),
    path('deleteType_identity/<int:pk>/', views.tType_identityDeleteView.as_view(),name='deleteType_identity'),
# Lenguajes
    path('tLanguage/', views.tLanguage_view, name='tLanguage'),
    path('createLanguage', views.tLanguageCreateView.as_view(),name='createLanguage'),
    path('updateLanguage/<int:pk>/', views.tLanguageUpdateView.as_view(),name='updateLanguage'),
    path('deleteLanguage/<int:pk>/', views.tLanguageDeleteView.as_view(),name='deleteLanguage'),
# Roles de transcripción
    path('tRoles_trans/', views.tRoles_trans_view, name='tRoles_trans'),
    path('createtRoles_trans', views.tRoles_transCreateView.as_view(),name='createtRoles_trans'),
    path('updatetRoles_trans/<int:pk>/', views.tRoles_transUpdateView.as_view(),name='updatetRoles_trans'),
    path('deletetRoles_trans/<int:pk>/', views.tRoles_transDeleteView.as_view(),name='deletetRoles_trans'),

# Etapas de transcripción
    path('tEtapas_trans/', views.tEtapas_trans_view, name='tEtapas_trans'),
    path('createtEtapas_trans', views.tEtapas_transCreateView.as_view(),name='createtEtapas_trans'),
    path('updatetEtapas_trans/<int:pk>/', views.tEtapas_transUpdateView.as_view(),name='updatetEtapas_trans'),
    path('deletetEtapas_trans/<int:pk>/', views.tEtapas_transDeleteView.as_view(),name='deletetEtapas_trans'),

# Transcripciones
    path('folder/<int:folder_id>/', views.folder_detail, name='folder_detail'),
    path('upload/', views.upload_file, name='upload_file'),

    path('tTranscript/', views.tTranscript_view, name='tTranscript'),
    path('createtTranscript', views.tTranscriptCreateView.as_view(),name='createtTranscript'),
    path('updatetTranscript/<int:pk>/', views.tTranscriptUpdateView.as_view(),name='updatetTranscript'),
    path('deletetTranscript/<int:pk>/', views.tTranscriptDeleteView.as_view(),name='deletetTranscript'),
    
# Personas

    path('tPerson/', views.tPerson_view, name='tPerson'),
    path('createtPerson', views.tPersonCreateView.as_view(),name='createtPerson'),
    path('updatetPerson/<int:pk>/', views.tPersonUpdateView.as_view(),name='updatetPerson'),
    path('deletetPerson/<int:pk>/', views.tPersonDeleteView.as_view(),name='deletetPerson'),

# Speakers

]

