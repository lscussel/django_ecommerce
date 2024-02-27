from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pedido(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.PROTECT)
  total = models.FloatField()
  status = models.CharField(
    max_length=1, 
    default='C',
    choices=(
      ('A', 'Aprovado'), 
      ('C', 'Criado'), 
      ('R', 'Reprovado'), 
      ('P', 'Pendente'), 
      ('E', 'Enviado'), 
      ('F', 'Finalizado'), 
    )
  )

  def __str__(self):
    return f'Pedido n. {self.pk}'

class ItemPedido(models.Model):
  pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
  produto = models.CharField(max_length=255)
  produto_id = models.PositiveIntegerField()
  variacao = models.CharField(max_length=255)
  variacao_id = models.PositiveIntegerField()
  preco = models.FloatField()
  quantidade = models.PositiveIntegerField()
  imagem = models.CharField(max_length=2000)

  class Meta:
    verbose_name = 'Item do pedido'
    verbose_name_plural = 'Itens do pedido'

  def __str__(self):
    return f'Item {self.pk} do {self.pedido}'