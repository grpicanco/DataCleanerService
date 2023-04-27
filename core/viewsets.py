from rest_framework import viewsets
from rest_framework.response import Response

from core import models, serializer, behavior as bv


class RegraViewSet(viewsets.ModelViewSet):
    queryset = models.Regra.objects.all()
    serializer_class = serializer.RegraSerializer


class AcaoDeCorrecaoViewSet(viewsets.ModelViewSet):
    queryset = models.AcaoDeCorrecao.objects.all()
    serializer_class = serializer.AcaoDeCorecaoSerializer


class ConjuntoDeDados(viewsets.ModelViewSet):
    serializer_class = serializer.ConjuntoDeDadosSerializer

    def create_conjunto_de_dados(self, request, *args, **kwargs):
        conjunto_de_dados = models.ConjuntoDeDados(
            dados=request.data['dados'],
            regras=models.Regra.objects.get(pk=request.data['regras']),
            acao_correcao=models.AcaoDeCorrecao.objects.get(pk=request.data['acao_de_correcao'])
        )
        behavior = bv.ExecutarRegraEAplicarAcao()
        resultado = behavior.run(conjunto_de_dados.dados, conjunto_de_dados.regras, conjunto_de_dados.acao_correcao)

        return Response({'resultado': resultado})
