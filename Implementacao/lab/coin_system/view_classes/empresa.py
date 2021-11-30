from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from coin_system.models import Empresa

#######
####### EMPRESA
#######

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