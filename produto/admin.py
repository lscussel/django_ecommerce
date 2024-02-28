from django.contrib import admin
from .models import Produto, Variacao


# Register your models here.
class VariacaoInline(admin.TabularInline):
  model = Variacao
  extra = 1

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
  list_display = [ 'nome', 'descricao_curta', 'get_preco_marketing', 'get_preco_promocional' ]
  inlines = [ VariacaoInline ]
  readonly_fields = ('slug',)

@admin.register(Variacao)
class VariacaoAdmin(admin.ModelAdmin):
  ...