from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from emprestimos.models import Emprestimo
from emprestimos.api.serializers import EmprestimoSerializer
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from usuarios.models import Usuario
from rest_framework.permissions import IsAuthenticated
from datetime import date


class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all().order_by('id')
    serializer_class = EmprestimoSerializer
    pagination_class = PageNumberPagination

    
# Views do Empréstimo por Usuário
class EmprestimoPorUsuarioAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    serializer_class = EmprestimoSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']
        return Emprestimo.objects.filter(usuario_id=usuario_id)
    
# Empréstimos em atraso de um Usuário
class EmprestimoEmAtraso(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    serializer_class = EmprestimoSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']
        usuario = get_object_or_404(Usuario, id=usuario_id)
        return Emprestimo.objects.filter(usuario=usuario, dData_devolucao__lt=date.today())
    
# Consultar Empréstimos realizados entre as datas de início e fim especificadas
class EmprestimoConsulta(ListAPIView):
    serializer_class = EmprestimoSerializer
    parser_classes = [JSONParser]

    def get_queryset(self):
        data_inicio = self.request.data.get('data_inicio')
        data_fim = self.request.data.get('data_fim')

        return Emprestimo.objects.filter(dData_emprestimo__gte=data_inicio, dData_emprestimo__lte=data_fim)