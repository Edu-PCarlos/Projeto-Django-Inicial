from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from people.models import Curso

class CursoListView(ListView):
    model = Curso
    template_name = 'people/curso_list.html' 

class CursoCreateView(CreateView):
    model = Curso
    fields = ['nome', 'descricao']
    template_name = 'people/curso_form.html'
    success_url = reverse_lazy('curso-list')

class CursoUpdateView(UpdateView):
    model = Curso
    fields = ['nome', 'descricao']
    template_name = 'people/curso_form.html'
    success_url = reverse_lazy('curso-list')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'people/curso_delete.html'
    success_url = reverse_lazy('curso-list')
