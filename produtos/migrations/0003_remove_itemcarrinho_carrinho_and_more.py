# Generated by Django 5.0.7 on 2024-12-13 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_carrinho_itemcarrinho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcarrinho',
            name='carrinho',
        ),
        migrations.RemoveField(
            model_name='itemcarrinho',
            name='produto',
        ),
        migrations.DeleteModel(
            name='Carrinho',
        ),
        migrations.DeleteModel(
            name='ItemCarrinho',
        ),
    ]
