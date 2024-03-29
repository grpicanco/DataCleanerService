# Generated by Django 4.2 on 2023-05-25 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcaoDeCorrecao',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('data_criacao', models.DateField(auto_now_add=True, db_column='dt_criacao', null=True, verbose_name='Criado em')),
                ('data_modificacao', models.DateField(auto_now_add=True, db_column='dt_modificacao', null=True, verbose_name='Modificado em')),
                ('titulo', models.CharField(db_column='tx_titulo', max_length=128, verbose_name='Título')),
                ('descricao', models.CharField(db_column='tx_descricao', max_length=128, verbose_name='Descrição')),
                ('tipo', models.CharField(choices=[('NUM', 'Numérico'), ('TXT', 'Texto'), ('DAT', 'Data'), ('MOE', 'Moeda')], db_column='tx_tipo', max_length=3)),
                ('script', models.TextField(db_column='tx_script', verbose_name='Script')),
            ],
            options={
                'verbose_name': 'Ações de Correções',
                'db_table': 'acao_de_correcao',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Regra',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('data_criacao', models.DateField(auto_now_add=True, db_column='dt_criacao', null=True, verbose_name='Criado em')),
                ('data_modificacao', models.DateField(auto_now_add=True, db_column='dt_modificacao', null=True, verbose_name='Modificado em')),
                ('titulo', models.CharField(db_column='tx_titulo', max_length=128, verbose_name='Título')),
                ('descricao', models.CharField(db_column='tx_descricao', max_length=128, verbose_name='Descrição')),
                ('tipo', models.CharField(choices=[('NUM', 'Numérico'), ('TXT', 'Texto'), ('DAT', 'Data'), ('MOE', 'Moeda')], db_column='tx_tipo', max_length=3)),
                ('script', models.TextField(db_column='tx_script', verbose_name='Script')),
            ],
            options={
                'verbose_name': 'Regras',
                'db_table': 'regra',
                'ordering': ['id'],
            },
        ),
    ]
