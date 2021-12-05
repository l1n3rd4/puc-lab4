from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from coin_system.models import Vantagem

#######
####### EMPRESA
#######

class VantagemListView(ListView):
    model = Vantagem
    template_name = 'vantagem/list.html'
    context_object_name = 'vantagens'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(VantagemListView, self).get_context_data(**kwargs)
        vantagens = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(vantagens, self.paginate_by)
        try:
            vantagens = paginator.page(page)
        except PageNotAnInteger:
            vantagens = paginator.page(1)
        except EmptyPage:
            vantagens = paginator.page(paginator.num_pages)
        context['vantagens'] = vantagens
        return context

class VantagemCreateView(CreateView):
    model = Vantagem
    template_name = 'vantagem/create.html'
    fields = ('nome', 'descricao', 'empresa', 'valor')
    success_url = reverse_lazy('vantagem-list')

class VantagemDetailView(DetailView):

    model = Vantagem
    template_name = 'vantagem/detail.html'
    context_object_name = 'vantagem'

class VantagemUpdateView(UpdateView):

    model = Vantagem
    template_name = 'vantagem/update.html'
    context_object_name = 'vantagem'
    fields = ('nome', 'descricao', 'empresa', 'valor')

    def get_success_url(self):
        return reverse_lazy('vantagem-detail', kwargs={'pk': self.object.id})

class VantagemDeleteView(DeleteView):
    model = Vantagem
    template_name = 'vantagem/delete.html'
    success_url = reverse_lazy('vantagem-list')