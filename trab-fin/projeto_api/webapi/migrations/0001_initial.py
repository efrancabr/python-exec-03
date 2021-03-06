# Generated by Django 3.1 on 2020-09-24 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContasReceber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_expectativa', models.DateField()),
                ('data_recebimento', models.DateField(null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('descricao', models.CharField(max_length=100)),
                ('situacao', models.CharField(max_length=50, null=True)),
                ('classificacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='classificacao_cr', to='webapi.classificacao')),
                ('forma_recebimento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='forma_recebimento_cr', to='webapi.formapagamento')),
            ],
        ),
        migrations.CreateModel(
            name='ContasPagar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_vencimento', models.DateField()),
                ('data_pagamento', models.DateField(null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('descricao', models.CharField(max_length=100)),
                ('situacao', models.CharField(max_length=50, null=True)),
                ('classificacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='classificacao_cp', to='webapi.classificacao')),
                ('forma_pagamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='forma_pagamento_cp', to='webapi.formapagamento')),
            ],
        ),
    ]
