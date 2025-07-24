from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from people.models import Aluno

class AlunoListView(ListView):
    model = Aluno
    template_name = 'people/aluno_list.html'

class AlunoCreateView(CreateView):
    model = Aluno
    fields = ['nome', 'email', 'curso']
    template_name = 'people/aluno_form.html'
    success_url = reverse_lazy('aluno-list')

class AlunoUpdateView(UpdateView):
    model = Aluno
    fields = ['nome', 'email', 'curso']
    template_name = 'people/aluno_form.html'
    success_url = reverse_lazy('aluno-list')

class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'people/aluno_delete.html'
    success_url = reverse_lazy('aluno-list')
