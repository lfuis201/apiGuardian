from drf_spectacular.utils import extend_schema
from .serializers import ManagerCreateSerializer
from .permissions import IsSuperAdmin
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status, generics

@extend_schema(
    request=ManagerCreateSerializer,
    responses={201: dict, 400: dict},
    tags=["Managers"],
    summary="Crear nuevo Manager",
    description="Solo el superadmin puede crear usuarios asignados automáticamente al grupo 'manager'."
)
class CreateManagerView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def post(self, request):
        serializer = ManagerCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Manager creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    responses={200: ManagerCreateSerializer(many=True)},
    tags=["Managers"],
    summary="Listar Managers",
    description="Devuelve una lista de todos los usuarios que pertenecen al grupo 'manager'. Solo accesible para superadmin."
)
class ListManagersView(generics.ListAPIView):
    serializer_class = ManagerCreateSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def get_queryset(self):
        return User.objects.filter(groups__name='manager')