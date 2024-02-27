from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
  model = ItemPedido
  extra = 1

# Register your models here.
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
  inlines = [ ItemPedidoInline ]

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
  ...