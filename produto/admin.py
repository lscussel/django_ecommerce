from django.contrib import admin
from .models import Produto, Variacao


# Register your models here.
class VariacaoInline(admin.TabularInline):
  model = Variacao
  extra = 1

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
  inlines = [ VariacaoInline ]

@admin.register(Variacao)
class VariacaoAdmin(admin.ModelAdmin):
  ...