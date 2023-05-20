from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from emprestimos.models import Emprestimo
from emprestimos.api.serializers import EmprestimoSerializer


class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all().order_by('id')
    serializer_class = EmprestimoSerializer
    pagination_class = PageNumberPagination