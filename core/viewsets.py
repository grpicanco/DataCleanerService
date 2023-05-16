from rest_framework import viewsets, status
from rest_framework.response import Response
from core import models, serializer, behavior as bv
from core.models import EscritaScript


class RegraViewSet(viewsets.ModelViewSet):
    queryset = models.Regra.objects.all()
    serializer_class = serializer.RegraSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            nova_regra = models.Regra.objects.get(pk=response.data['id'])
            tipo_descricao = nova_regra.get_tipo_display()
            escrita_script = EscritaScript(tipo_descricao)
            escrita_script.criar_funcao(nova_regra)

        return response


class AcaoDeCorrecaoViewSet(viewsets.ModelViewSet):
    queryset = models.AcaoDeCorrecao.objects.all()
    serializer_class = serializer.AcaoDeCorecaoSerializer


class ConjuntoDeDados(viewsets.ModelViewSet):
    serializer_class = serializer.ConjuntoDeDadosSerializer

    def create(self, request, *args, **kwargs):
        dados = request.data.get('dados', None)
        regras_ids = request.data.get('regras', None)
        acao_correcoes_id = request.data.get('acao_correcao', None)

        # Verifica se o campo 'dados' está presente nos dados recebidos
        if dados is None:
            return Response({'error': 'O campo "dados" é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        regras = None
        if regras_ids is not None:
            try:
                regras = models.Regra.objects.filter(pk__in=regras_ids)
            except models.Regra.DoesNotExist:
                return Response({'error': f'Algumas das regras informadas não existem.'},
                                status=status.HTTP_400_BAD_REQUEST)

        acao_correcoes = None
        if acao_correcoes_id is not None:
            try:
                acao_correcoes = models.AcaoDeCorrecao.objects.filter(pk__in=acao_correcoes_id)
            except models.AcaoDeCorrecao.DoesNotExist:
                return Response({'error': f'Algumas das a informadas não existem.'},
                                status=status.HTTP_400_BAD_REQUEST)

        conjunto_de_dados = models.ConjuntoDeDados(
            dados=dados,
            regras=regras,
            acao_correcao=acao_correcoes
        )

        behavior = bv.ExecutarRegra()
        resultado = behavior.run(conjunto_de_dados)
        return Response({'resultado': resultado})
