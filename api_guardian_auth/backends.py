from axes.backends import AxesBackend
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from axes.helpers import get_client_username
from axes.handlers.proxy import AxesProxyHandler

User = get_user_model()

class CustomAxesBackend(AxesBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if AxesProxyHandler.is_locked(request, credentials={'username': username}):
            raise AuthenticationFailed("Demasiados intentos fallidos. Tu cuenta o IP ha sido bloqueada temporalmente.")
        return super().authenticate(request, username, password, **kwargs)
