from django.db import models
from livros.models import Livro
from usuarios.models import Usuario

class Emprestimo(models.Model):
    id = models.AutoField(primary_key=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    dData_emprestimo = models.DateField()
    dData_devolucao = models.DateField()

    def __str__(self):
        return f'Usuário: {self.usuario}, Livro: {self.livro}, Data de empréstimo: {self.dData_emprestimo}, Data de devolução: {self.dData_devolucao}'