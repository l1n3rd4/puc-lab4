from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from coin_system.models import Professor

#######
####### PROFESSOR
#######

class ProfessorListView(ListView):
    model = Professor
    template_name = 'professor/list.html'
    context_object_name = 'professores'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ProfessorListView, self).get_context_data(**kwargs)
        professores = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(professores, self.paginate_by)
        try:
            professores = paginator.page(page)
        except PageNotAnInteger:
            professores = paginator.page(1)
        except EmptyPage:
            professores = paginator.page(paginator.num_pages)
        context['professores'] = professores
        return context

class ProfessorCreateView(CreateView):
    model = Professor
    template_name = 'professor/create.html'
    fields = ('nome', 'cpf', 'departamento', 'instituicao_ensino', 'saldo')
    success_url = reverse_lazy('professor-list')

class ProfessorDetailView(DetailView):

    model = Professor
    template_name = 'professor/detail.html'
    context_object_name = 'aluno'

class ProfessorUpdateView(UpdateView):

    model = Professor
    template_name = 'professor/update.html'
    context_object_name = 'aluno'
    fields = ('nome', 'cpf', 'departamento', 'instituicao_ensino', 'saldo')

    def get_success_url(self):
        return reverse_lazy('professor-detail', kwargs={'pk': self.object.id})

class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = 'professor/delete.html'
    success_url = reverse_lazy('professor-list')