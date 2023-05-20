from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    vNome = models.CharField(max_length=80)
    dNascimento = models.DateField()
    vCpf = models.CharField(max_length=11, unique=True)
    vEmail = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'Nome: {self.vNome}, CPF: {self.vCpf}, E-mail: {self.vEmail}'