from django.shortcuts import render
from django.views.generic import *
from app.models import *

class HomeView(TemplateView):
    template_name = 'index.html'

class CategoriaListView(ListView):
    template_name = 'produtos/categorias.html'
    context_object_name = 'categorias'  
    model = Categoria   

class ProdutosListView(ListView):
    model = Produto
    template_name = 'produtos/listarprodutos.html'
    context_object_name = 'produtos'
    queryset = Produto.disponiveis.all()
    
    def get_queryset(self, slugcat=None):
        qs = super().get_queryset()
        if slugcat:
            cat = Categoria.get(slug=slugcat)
            qs = qs.filter(categoria=cat)
        return qs
    
    def get_context_data(self, slugcat=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if slugcat:
            context['categoria'] = Categoria.objects.get(slug=slugcat)
        return context