# Generated by Django 5.0.7 on 2024-12-24 13:30

import datetime
import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=65, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=80, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('capa', models.ImageField(blank=True, null=True, upload_to='capa/%Y/%m/%d/')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produtos.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True, default=1, null=True)),
                ('endereco', models.TextField()),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('data', models.DateField(default=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.cliente')),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('old_cart', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
