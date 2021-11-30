from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from coin_system.models import Aluno

#######
####### ALUNO
#######

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