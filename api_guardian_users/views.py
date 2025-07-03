from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
from drf_spectacular.utils import extend_schema
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics

from .serializers import ManagerCreateSerializer
from .permissions import IsSuperAdmin


@method_decorator(ratelimit(key='ip', rate='5/m', block=False), name='dispatch')
@extend_schema(
    request=ManagerCreateSerializer,
    responses={
        201: {"type": "object", "properties": {"detail": {"type": "string"}}},
        400: {"type": "object"},
        401: {"type": "object", "properties": {"detail": {"type": "string"}}},
        403: {"type": "object", "properties": {"detail": {"type": "string"}}},
        429: {"type": "object", "properties": {"detail": {"type": "string"}}},
    },
    tags=["Managers"],
    summary="Crear nuevo Manager",
    description="Solo el superadmin puede crear usuarios. Límite: 5 solicitudes por minuto."
)
class CreateManagerView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def dispatch(self, request, *args, **kwargs):
        if getattr(request, 'limited', False):
            request = self.initialize_request(request, *args, **kwargs)
            response = Response(
                {"detail": "Límite excedido para esta ruta. Espera un momento antes de volver a intentarlo."},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )
            response.accepted_renderer = self.get_renderers()[0]
            response.accepted_media_type = response.accepted_renderer.media_type
            response.renderer_context = self.get_renderer_context()
            return response
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        serializer = ManagerCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Manager creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(ratelimit(key='ip', rate='10/m', block=False), name='dispatch')
@extend_schema(
    responses={
        200: ManagerCreateSerializer(many=True),
        401: {"type": "object", "properties": {"detail": {"type": "string"}}},
        403: {"type": "object", "properties": {"detail": {"type": "string"}}},
        429: {"type": "object", "properties": {"detail": {"type": "string"}}},
    },
    tags=["Managers"],
    summary="Listar Managers",
    description="Devuelve una lista de managers. Solo accesible para superadmin. Límite: 10 solicitudes por minuto."
)
class ListManagersView(generics.ListAPIView):
    serializer_class = ManagerCreateSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def dispatch(self, request, *args, **kwargs):
        if getattr(request, 'limited', False):
            request = self.initialize_request(request, *args, **kwargs)
            response = Response(
                {"detail": "Límite excedido para esta ruta. Espera un momento antes de volver a intentarlo."},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )
            response.accepted_renderer = self.get_renderers()[0]
            response.accepted_media_type = response.accepted_renderer.media_type
            response.renderer_context = self.get_renderer_context()
            return response
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return User.objects.filter(groups__name='manager')
