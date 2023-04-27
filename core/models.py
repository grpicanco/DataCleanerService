from typing import List

from django.db import models
from django.utils.translation import gettext as _


class NullCharField(models.CharField):
    def get_prep_value(self, value):
        if value == '':
            return None
        return value


class ModelBase(models.Model):
    id = models.IntegerField(
        db_column='id',
        primary_key=True
    )
    data_criacao = models.DateField(
        db_column='dt_criacao',
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name=_('Criado em')
    )
    data_modificacao = models.DateField(
        db_column='dt_modificacao',
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name=_('Modificado em')
    )


class Tipo(models.TextChoices):
    NUM = 'NUM', _('Numérico')
    TXT = 'TXT', _('Texto')
    DAT = 'DAT', _('Data')
    MOE = 'MOE', _('Moeda')


# Create your models here.
class Regra(ModelBase):
    titulo = models.CharField(
        db_column='tx_titulo',
        null=False,
        blank=False,
        max_length=128,
        verbose_name=_('Título')
    )
    descricao = models.CharField(
        db_column='tx_descricao',
        null=False,
        blank=False,
        max_length=128,
        verbose_name=_('Descrição')
    )
    tipo = models.CharField(
        db_column='tx_tipo',
        null=False,
        blank=False,
        max_length=3,
        choices=Tipo.choices,
    )
    script = models.TextField(
        db_column='tx_script',
        null=False,
        blank=False,
        verbose_name=_('Script')
    )


class AcaoDeCorrecao(ModelBase):
    titulo = models.CharField(
        db_column='tx_titulo',
        null=False,
        blank=False,
        max_length=128,
        verbose_name=_('Título')
    )
    descricao = models.CharField(
        db_column='tx_descricao',
        null=False,
        blank=False,
        max_length=128,
        verbose_name=_('Descrição')
    )
    tipo = models.CharField(
        db_column='tx_tipo',
        null=False,
        blank=False,
        max_length=3,
        choices=Tipo.choices,
    )
    script = models.TextField(
        db_column='tx_script',
        null=False,
        blank=False,
        verbose_name=_('Script')
    )


class ConjuntoDeDados:
    def __init__(self, dados: List, regras: List[Regra], acao_correcao: List[AcaoDeCorrecao]):
        self.dados = dados
        self.regras = regras
        self.acao_correcao = acao_correcao
