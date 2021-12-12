"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from coin_system import views
from coin_system.view_classes import aluno, empresa, professor, vantagem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('minhas-moedas', views.my_coins, name='minhas-moedas'),
    path('trocar-moedas', views.exchange_coins, name='trocar-moedas'),
    path('cadastrar-vantagem', views.empresa_create_vantagem, name='cadastrar-vantagem'),
    path('minhas-vantagens', views.empresa_minhas_vantagens, name='minhas-vantagens'),
    path('cadastro/<slug:registration_type>', views.cadastro, name='cadastro'),

    path('alunos', aluno.AlunoListView.as_view(), name='aluno-list'),
    path('aluno/novo', aluno.AlunoCreateView.as_view(), name='aluno-new'),
    path('aluno/<int:pk>', aluno.AlunoDetailView.as_view(), name='aluno-details'),
    path('aluno/editar/<int:pk>', aluno.AlunoUpdateView.as_view(), name='aluno-update'),
    path('aluno/deletar/<int:pk>', aluno.AlunoDeleteView.as_view(), name='aluno-delete'),

    path('empresas', empresa.EmpresaListView.as_view(), name='empresa-list'),
    path('empresa/novo', empresa.EmpresaCreateView.as_view(), name='empresa-new'),
    path('empresa/<int:pk>', empresa.EmpresaDetailView.as_view(), name='empresa-details'),
    path('empresa/editar/<int:pk>', empresa.EmpresaUpdateView.as_view(), name='empresa-update'),
    path('empresa/deletar/<int:pk>', empresa.EmpresaDeleteView.as_view(), name='empresa-delete'),

    path('vantagens', vantagem.VantagemListView.as_view(), name='vantagem-list'),
    path('vantagem/novo', vantagem.VantagemCreateView.as_view(), name='vantagem-new'),
    path('vantagem/<int:pk>', vantagem.VantagemDetailView.as_view(), name='vantagem-details'),
    path('vantagem/editar/<int:pk>', vantagem.VantagemUpdateView.as_view(), name='vantagem-update'),
    path('vantagem/deletar/<int:pk>', vantagem.VantagemDeleteView.as_view(), name='vantagem-delete'),

    path('professores', professor.ProfessorListView.as_view(), name='professor-list'),
    path('professor/novo', professor.ProfessorCreateView.as_view(), name='professor-new'),
    path('professor/<int:pk>', professor.ProfessorDetailView.as_view(), name='professor-details'),
    path('professor/editar/<int:pk>', professor.ProfessorUpdateView.as_view(), name='professor-update'),
    path('professor/deletar/<int:pk>', professor.ProfessorDeleteView.as_view(), name='professor-delete')
]
