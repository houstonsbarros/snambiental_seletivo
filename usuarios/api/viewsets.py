from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from usuarios.models import Usuario
from usuarios.api.serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer
    pagination_class = PageNumberPagination