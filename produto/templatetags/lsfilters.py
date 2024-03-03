from django.template import Library
from utils import utils

register = Library()

@register.filter
def formata_preco(valor):
  return utils.formata_preco(valor)

@register.filter
def total_itens_carrinho(carrinho):
  return utils.total_itens_carrinho(carrinho)
