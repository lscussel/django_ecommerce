from typing import Iterable
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from PIL import Image
import os
from utils import utils

# Create your models here.
class Produto(models.Model):
  nome = models.CharField(max_length=255)
  descricao_curta = models.TextField(max_length=255)
  descricao_longa = models.TextField(blank=True)
  imagem = models.ImageField(upload_to='produto_imagens/%Y/%m', blank=True, null=True)
  slug = models.SlugField(unique=True, blank=True)
  preco_marketing = models.FloatField(verbose_name='Preço')
  preco_marketing_promocional = models.FloatField(default=0, verbose_name='Preço promocional')
  tipo = models.CharField(default='V', max_length=1, choices=(('V', 'Variável'), ('S', 'Simples'),))

  def get_preco_marketing(self):
    return utils.formata_preco(self.preco_marketing)
  get_preco_marketing.short_description = 'Preço'
  
  def get_preco_promocional(self):
    return utils.formata_preco(self.preco_marketing_promocional)
  get_preco_promocional.short_description = 'Preço promocional'

  @staticmethod
  def resize_image(img, new_width=800):
    img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
    img_pil = Image.open(img_full_path)
    original_width, original_height = img_pil.size

    if original_width <= new_width:
      img_pil.close()
      return 
    
    new_height = round((new_width * original_height) / original_width)
    new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
    new_img.save(img_full_path, optimize=True, quality=50)

  def save(self, *args, **kwargs):
    slug_antes_salvar = self.slug
    super().save(*args, **kwargs)

    if not slug_antes_salvar:
      self.slug = slugify(f'{self.nome}-{self.pk}')
      super().save(*args, **kwargs)

    if self.imagem:
      self.resize_image(self.imagem)

  def __str__(self):
    return self.nome
  
class Variacao(models.Model):
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  nome = models.CharField(max_length=50, blank=True, null=True)
  preco = models.FloatField()
  preco_promocional = models.FloatField(default=0)
  estoque = models.PositiveIntegerField(default=1)

  class Meta:
    verbose_name = 'Variação'
    verbose_name_plural = 'Variações'

  def __str__(self):
    return self.nome or self.produto.nome
  