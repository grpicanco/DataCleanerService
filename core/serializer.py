from rest_framework import serializers
from core.models import Regra, AcaoDeCorrecao


class RegraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regra
        fields = '__all__'


class AcaoDeCorecaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcaoDeCorrecao
        fields = '__all__'


class ConjuntoDeDadosSerializer(serializers.Serializer):
    dados = serializers.ListField()
    regras = serializers.PrimaryKeyRelatedField(queryset=Regra.objects.all(), required=False, allow_null=True,
                                                many=True)
    acao_correcao = serializers.PrimaryKeyRelatedField(queryset=AcaoDeCorrecao.objects.all(), required=False,
                                                       allow_null=True, many=True)
