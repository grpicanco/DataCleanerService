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
    regras = serializers.HyperlinkedRelatedField(
        queryset=Regra.objects.all(),
        required=False,
        allow_null=True,
        many=True,
        read_only=False,
        view_name='RegraViewSet',
    )
    acao_correcao = serializers.HyperlinkedRelatedField(
        queryset=AcaoDeCorrecao.objects.all(),
        required=False,
        allow_null=True,
        many=True,
        read_only=False,
        view_name='AcaoDeCorrecaoViewSet',
    )
