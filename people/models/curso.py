from django.db import models
from .base import BaseModel

class Curso(BaseModel):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome