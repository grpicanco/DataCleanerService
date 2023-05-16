from typing import List

from core.models import ConjuntoDeDados


class ExecutarRegra:
    @staticmethod
    def __aplicar_regras(regra, dados: List):
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
    def run(conjunto_de_dados: ConjuntoDeDados):
        values = {}
        for regra in conjunto_de_dados.regras:
            (correto, errado) = ExecutarRegra.__aplicar_regras(regra=regra, dados=conjunto_de_dados.dados)
            values['correto'] = correto
            values['errado'] = errado

        return values
