# Generated by Django 5.0.2 on 2024-02-28 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_produto_descricao_longa_alter_produto_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m'),
        ),
    ]
