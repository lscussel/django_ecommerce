from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from . import models

# Create your views here.
class ListaProdutos(ListView):
  model = models.Produto
  template_name = 'produto/lista.html'
  context_object_name = 'produtos'
  paginate_by = 10

class DetalheProduto(View):
  ...

class AdicionarAoCarrinho(View):
  ...

class RemoverDoCarrinho(View):
  ...

class Carrinho(View):
  ...

class Finalizar(View):
  ...