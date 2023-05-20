from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from livros.models import Livro
from livros.api.serializers import LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all().order_by('id')
    serializer_class = LivroSerializer
    pagination_class = PageNumberPagination