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
    def __aplica_regra(correto, errado, conjunto_de_dados):
        for regra in conjunto_de_dados.regras:
            (value_correto, value_errado) = ExecutarLimpeza.__regras(regra=regra, dados=conjunto_de_dados.dados)
            correto.extend(value_correto)
            errado.extend(value_errado)
        return correto, errado

    @staticmethod
    def __aplica_acao_de_correcao(errado, conjunto_de_dados):
        corrigido = []
        nao_corrigido = errado if conjunto_de_dados.regras else conjunto_de_dados.dados

        for acao_correcao in conjunto_de_dados.acoes_correcoes:
            (values_corrigido, values_nao_corrigido) = ExecutarLimpeza.__acao_correcao(acao_de_correcao=acao_correcao,
                                                                         dados=nao_corrigido)
            # Adiciona os valores corrigidos a lista de correto
            corrigido.extend(values_corrigido)

            # Remove valores correspondentes da lista 'errado'
            valores_a_remover = {item[0] for item in corrigido if item[0] is not None}
            nao_corrigido = [item for item in errado if item[0] not in valores_a_remover]
        return corrigido, nao_corrigido

    @staticmethod
    def __ordena_dados(values):
        values['correto'] = sorted(values['correto'], key=lambda x: x[0])
        values['errado'] = sorted(values['errado'], key=lambda x: x[0])
        values['corrigido'] = sorted(values['corrigido'], key=lambda x: x[0])
        values['nao_corrigido'] = sorted(values['nao_corrigido'], key=lambda x: x[0])
        values['dados'] = sorted(values['dados'], key=lambda x: x[0])

    @staticmethod
    def run(conjunto_de_dados: ConjuntoDeDados):
        correto = []
        errado = []
        corrigido = []
        nao_corrigido = []

        if conjunto_de_dados.regras:
            correto, errado = ExecutarLimpeza.__aplica_regra(correto, errado, conjunto_de_dados)

        if conjunto_de_dados.acoes_correcoes:
            corrigido, nao_corrigido = ExecutarLimpeza.__aplica_acao_de_correcao(errado, conjunto_de_dados)

        if conjunto_de_dados.regras or conjunto_de_dados.acoes_correcoes:
            dados = correto + corrigido + nao_corrigido
        else:
            dados = conjunto_de_dados.dados

        values = {
            'correto': correto,
            'errado': errado,
            'corrigido': corrigido,
            'nao_corrigido': nao_corrigido,
            'dados': dados
        }

        if values:
            ExecutarLimpeza.__ordena_dados(values)

        return values
