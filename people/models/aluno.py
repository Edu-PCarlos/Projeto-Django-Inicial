from django.db import models
from .base import BaseModel
from .curso import Curso

class Aluno(BaseModel):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome