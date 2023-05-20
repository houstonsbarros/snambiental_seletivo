from django.db import models

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    vTitulo = models.CharField(max_length=35)
    vAutor = models.CharField(max_length=20)
    iAno_publicacao = models.IntegerField()
    vEditora = models.CharField(max_length=15)

    def __str__(self):
        return f'Título: {self.vTitulo}, Autor: {self.vAutor}, Ano de publicação: {self.iAno_publicacao}, Editora: {self.vEditora}'