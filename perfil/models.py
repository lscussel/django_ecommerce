from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
  usuario = models.OneToOneField(User, on_delete=models.PROTECT)
  data_nascimento = models.DateField()
  cpf = models.CharField(max_length=11)
  endereco = models.CharField(max_length=34)
  numero = models.CharField(max_length=8)
  complemento = models.CharField(max_length=8)
  bairro = models.CharField(max_length=30)
  cep = models.CharField(max_length=8)
  cidade = models.CharField(max_length=30)
  estado = models.CharField(
    max_length=2, 
    choices=(
      ('AC', 'Acre'),
      ('AL', 'Alagoas'),
      ('AP', 'Amapá'),
      ('AM', 'Amazonas'),
      ('BA', 'Bahia'),
      ('CE', 'Ceará'),
      ('DF', 'Distrito Federal'),
      ('ES', 'Espírito Santo'),
      ('GO', 'Goiás'),
      ('MA', 'Maranhão'),
      ('MT', 'Mato Grosso'),
      ('MS', 'Mato Grosso do Sul'),
      ('MG', 'Minas Gerais'),
      ('PA', 'Pará'),
      ('PB', 'Paraíba'),
      ('PR', 'Paraná'),
      ('PE', 'Pernambuco'),
      ('PI', 'Piauí'),
      ('RN', 'Rio de Janeiro'),
      ('RS', 'Rio Grande do Norte'),
      ('RJ', 'Rio Grande do Sul'),
      ('RO', 'Rondônia'),
      ('RR', 'Roraima'),
      ('SC', 'Santa Catarina'),
      ('SP', 'São Paulo'),
      ('SE', 'Sergipe'),
      ('TO', 'Tocantins'),
    )
  )

  class Meta:
    verbose_name = 'Perfil'
    verbose_name_plural = 'Perfis'

  def __str__(self):
    return f'{self.usuario.first_name} {self.usuario.last_name}'
  
  def clean(self):
    ...