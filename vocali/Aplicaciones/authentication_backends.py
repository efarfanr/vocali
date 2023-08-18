from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import PermissionDenied
from .models import Usr_company

class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)
        if user:
            try:
                usr_company = Usr_company.objects.get(user=user)
                if not usr_company.enable:
                    raise PermissionDenied('Este usuario está inactivo')
            except Usr_company.DoesNotExist:
                raise PermissionDenied('El usuario no está asociado a ninguna empresa')
        return user






