from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from core import models, serializer, behavior as bv
from core.models import Regra, AcaoDeCorrecao


class RegraViewSet(viewsets.ModelViewSet):
    queryset = models.Regra.objects.all()
    serializer_class = serializer.RegraSerializer


class AcaoDeCorrecaoViewSet(viewsets.ModelViewSet):
    queryset = models.AcaoDeCorrecao.objects.all()
    serializer_class = serializer.AcaoDeCorecaoSerializer


class ConjuntoDeDados(viewsets.ModelViewSet):
    serializer_class = serializer.ConjuntoDeDadosSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        # Retorna uma resposta de método não permitido para requisições GET
        return Response({'detail': 'Método GET não permitido.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        # Retorna uma resposta de método não permitido para requisições GET de um objeto específico
        return Response({'detail': 'Método GET não permitido.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        # Retorna uma resposta de método não permitido para requisições PUT
        return Response({'detail': 'Método PUT não permitido.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        # Retorna uma resposta de método não permitido para requisições PATCH
        return Response({'detail': 'Método PATCH não permitido.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        # Retorna uma resposta de método não permitido para requisições DELETE
        return Response({'detail': 'Método DELETE não permitido.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        dados = request.data.get('dados', None)
        regras_urls = request.data.get('regras', None)
        acao_correcoes_urls = request.data.get('acao_correcao', None)

        # Verifica se o campo 'dados' está presente nos dados recebidos
        if dados is None:
            return Response({'error': 'O campo "dados" é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        regras = self.get_related_objects(self, urls=regras_urls, model=Regra)
        acao_correcoes = self.get_related_objects(self, urls=acao_correcoes_urls, model=AcaoDeCorrecao)

        conjunto_de_dados = models.ConjuntoDeDados(
            dados=dados,
            regras=regras,
            acoes_correcoes=acao_correcoes
        )

        behavior = bv.ExecutarLimpeza()
        resultado = behavior.run(conjunto_de_dados)
        return Response(resultado)

    @staticmethod
    def get_related_objects(self, urls, model):
        if urls is None:
            return []

        objects = []
        for url in urls:
            try:
                obj = self.get_object_from_url(url, model)
                objects.append(obj)
            except (ValueError, model.DoesNotExist):
                return Response(
                    {'error': f'Algumas das URLs fornecidas são inválidas ou os objetos relacionados não existem.'},
                    status=status.HTTP_400_BAD_REQUEST)

        return objects

    @staticmethod
    def get_object_from_url(url, model):
        pk = url.split('/')[-2]
        obj = model.objects.get(pk=pk)
        return obj
