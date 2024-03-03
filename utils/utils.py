def formata_preco(valor):
  return f'R$ {valor:.2f}'.replace('.', ',')

def total_itens_carrinho(carrinho):
  return sum([item['quantidade'] for item in carrinho.values()])