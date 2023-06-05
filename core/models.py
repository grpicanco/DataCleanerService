from typing import List

from django.db import models
from django.utils.translation import gettext as _


class NullCharField(models.CharField):
    def get_prep_value(self, value):
        if value == '':
            return None
        return value


class ModelBase(models.Model):
    id = models.BigAutoField(
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
    codigo = models.CharField(
        db_column='tx_codigo',
        blank=True,
        null=False,
        verbose_name=_('Código'),
        max_length=6,
        unique=True
    )

    class Meta:
        abstract = True


class Tipo(models.TextChoices):
    INT = 'INT', _('Numérico Inteiro')
    TXT = 'TXT', _('Texto')
    DAT = 'DAT', _('Data')
    MOE = 'MOE', _('Moeda')
    DEC = 'DEC', _('Decimal')
    POR = 'POR', _('Porcentagem')
    HOR = 'HOR', _('Hora')


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

    class Meta:
        db_table = 'regra'
        ordering = ['id']
        verbose_name = _('Regra')
        verbose_name_plural = _('Regras')


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

    class Meta:
        db_table = 'acao_de_correcao'
        ordering = ['id']
        verbose_name = _('Ação de Correção')
        verbose_name_plural = _('Ações de Correção')



class ConjuntoDeDados:
    def __init__(self, dados: List, regras: List[Regra], acoes_correcoes: List[AcaoDeCorrecao]):
        self.dados = dados
        self.regras = regras
        self.acoes_correcoes = acoes_correcoes
