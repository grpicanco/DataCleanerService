from typing import List

from core.models import ConjuntoDeDados


class ExecutarLimpeza:
    @staticmethod
    def __regras(regra, dados: List):
        correto = []
        errado = []
        local_dict = {'value': None}

        for i, elemento in enumerate(dados):
            local_dict['elemento'] = elemento
            exec(regra.script, None, local_dict)
            result = local_dict['value']
            if result:
                correto.append((i, local_dict['elemento']))
            else:
                errado.append((i, local_dict['elemento']))
        return correto, errado

    @staticmethod
    def __acao_correcao(acao_de_correcao, dados: List):
        corrigido = []
        nao_corrigido = []
        local_dict = {'value': None, 'elemento': None}
        for i, elemento in dados:
            local_dict['elemento'] = elemento
            exec(acao_de_correcao.script, None, local_dict)
            result = local_dict['value']
            # Valida de acordo com result o que irá fazer.
            corrigido.append((i, local_dict['elemento'])) if result else nao_corrigido.append(
                (i, local_dict['elemento']))
        return corrigido, nao_corrigido

    @staticmethod
    def __aplica_regra(values, conjunto_de_dados):
        for regra in conjunto_de_dados.regras:
            (correto, errado) = ExecutarLimpeza.__regras(regra=regra, dados=conjunto_de_dados.dados)
            values['correto'] = correto
            values['errado'] = errado
        return values

    @staticmethod
    def __aplica_acao_de_correcao(values, conjunto_de_dados):
        dados_de_correcao = values['errado'] if conjunto_de_dados.regras else conjunto_de_dados.dados

        for acao_correcao in conjunto_de_dados.acoes_correcoes:
            (corrigido, nao_corrigido) = ExecutarLimpeza.__acao_correcao(acao_de_correcao=acao_correcao,
                                                                         dados=dados_de_correcao)
            # Adiciona os valores corrigidos a lista de correto
            values['correto'].extend(corrigido)

            # Remove valores correspondentes da lista 'errado'
            valores_a_remover = {item[0] for item in corrigido if item[0] is not None}
            values['errado'] = [item for item in values['errado'] if item[0] not in valores_a_remover]
        return values

    @staticmethod
    def __ordena_dados(values):
        values['correto'] = sorted(values['correto'], key=lambda x: x[0])
        values['errado'] = sorted(values['errado'], key=lambda x: x[0])

    @staticmethod
    def run(conjunto_de_dados: ConjuntoDeDados):
        values = {}
        if conjunto_de_dados.regras:
            ExecutarLimpeza.__aplica_regra(values, conjunto_de_dados)

        if conjunto_de_dados.acoes_correcoes:
            ExecutarLimpeza.__aplica_acao_de_correcao(values, conjunto_de_dados)

        if values:
            ExecutarLimpeza.__ordena_dados(values)

        return values
