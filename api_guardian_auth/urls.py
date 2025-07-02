from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import ProtectedHelloView

urlpatterns = [
    # Autenticación básica: login/logout/password
    path('', include('dj_rest_auth.urls')),

    # Registro de usuario
    path('register/', include('dj_rest_auth.registration.urls')),

    # JWT refresh y verify
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Ruta protegida de prueba
    path('hello/', ProtectedHelloView.as_view(), name='hello'),
]
