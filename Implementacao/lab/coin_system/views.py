from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Aluno, Empresa

def home(request):
    return render(request, "authentication/index.html")

def signin(request):
    return render(request, "authentication/signin.html") 

def signup(request):
    return render(request, "authentication/signup.html") 

def signout(request):
    pass


class AlunoListView(ListView):
    model = Aluno
    template_name = 'aluno/list.html'
    context_object_name = 'alunos'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(AlunoListView, self).get_context_data(**kwargs)
        alunos = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(alunos, self.paginate_by)
        try:
            alunos = paginator.page(page)
        except PageNotAnInteger:
            alunos = paginator.page(1)
        except EmptyPage:
            alunos = paginator.page(paginator.num_pages)
        context['alunos'] = alunos
        return context

class AlunoCreateView(CreateView):
    model = Aluno
    template_name = 'aluno/create.html'
    fields = ('nome', 'email', 'cpf', 'rg', 'endereco', 'instituicao_ensino', 'curso', 'saldo')
    success_url = reverse_lazy('aluno-list')

class AlunoDetailView(DetailView):

    model = Aluno
    template_name = 'aluno/detail.html'
    context_object_name = 'aluno'

class AlunoUpdateView(UpdateView):

    model = Aluno
    template_name = 'aluno/update.html'
    context_object_name = 'aluno'
    fields = ('nome', 'email', 'cpf', 'rg', 'endereco', 'instituicao_ensino', 'curso', 'saldo')

    def get_success_url(self):
        return reverse_lazy('aluno-detail', kwargs={'pk': self.object.id})

class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'aluno/delete.html'
    success_url = reverse_lazy('aluno-list')



class EmpresaListView(ListView):
    model = Empresa
    template_name = 'empresa/list.html'
    context_object_name = 'empresas'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(EmpresaListView, self).get_context_data(**kwargs)
        empresas = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(empresas, self.paginate_by)
        try:
            empresas = paginator.page(page)
        except PageNotAnInteger:
            empresas = paginator.page(1)
        except EmptyPage:
            empresas = paginator.page(paginator.num_pages)
        context['empresas'] = empresas
        return context

class EmpresaCreateView(CreateView):
    model = Empresa
    template_name = 'empresa/create.html'
    fields = ('nome',)
    success_url = reverse_lazy('empresa-list')

class EmpresaDetailView(DetailView):

    model = Empresa
    template_name = 'empresa/detail.html'
    context_object_name = 'empresa'

class EmpresaUpdateView(UpdateView):

    model = Empresa
    template_name = 'empresa/update.html'
    context_object_name = 'empresa'
    fields = ('nome',)

    def get_success_url(self):
        return reverse_lazy('aluno-detail', kwargs={'pk': self.object.id})

class EmpresaDeleteView(DeleteView):
    model = Empresa
    template_name = 'empresa/delete.html'
    success_url = reverse_lazy('empresa-list')