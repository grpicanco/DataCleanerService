from rest_framework import serializers
from core.models import Regra, AcaoDeCorrecao


class RegraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regra
        fields = '__all__'


class AcaoDeCorecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcaoDeCorrecao
        fields = '__all__'


class ConjuntoDeDadosSerializer(serializers.Serializer):
    dados = serializers.ListField()
    regras = RegraSerializer()
    acao_correcao = AcaoDeCorrecao()
