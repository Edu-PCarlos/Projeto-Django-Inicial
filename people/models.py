from django.db import models

class Curso(models.Model):
   nome = models.CharField(max_length=100)

   def __str__(self):
       return self.nome

class Aluno(models.Model):
   nome = models.CharField(max_length=100)
   idade = models.IntegerField()
   curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

   def __str__(self):
       return f"{self.nome} - {self.curso.nome}"

   def apresentar(self):
       return f"Sou {self.nome}, tenho {self.idade} anos e faço {self.curso.nome}."
    