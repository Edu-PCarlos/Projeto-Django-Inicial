from django.urls import path
from .views import (
    CursoListView, CursoCreateView, CursoUpdateView, CursoDeleteView,
    AlunoListView, AlunoCreateView, AlunoUpdateView, AlunoDeleteView,
)

urlpatterns = [
    # Cursos
    path('cursos/', CursoListView.as_view(), name='curso-list'),
    path('cursos/novo/', CursoCreateView.as_view(), name='curso-create'),
    path('cursos/<int:pk>/editar/', CursoUpdateView.as_view(), name='curso-update'),
    path('cursos/<int:pk>/deletar/', CursoDeleteView.as_view(), name='curso-delete'),

    # Alunos
    path('alunos/', AlunoListView.as_view(), name='aluno-list'),
    path('alunos/novo/', AlunoCreateView.as_view(), name='aluno-create'),
    path('alunos/<int:pk>/editar/', AlunoUpdateView.as_view(), name='aluno-update'),
    path('alunos/<int:pk>/deletar/', AlunoDeleteView.as_view(), name='aluno-delete'),
]
