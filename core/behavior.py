from typing import List
from core.models import Regra, AcaoDeCorrecao


class ExecutarRegra:
    @staticmethod
    def __aplicar_regras(regra, values: List):
        script = regra.script
        print(script)
        codigo_compilado = compile(script, '<string>', 'exec')
        correto, errado = exec(codigo_compilado, {'dados': values})
        print(correto, errado)
        return correto, errado

    @staticmethod
    def run(conjunto_de_dados: List, regras: List[Regra], acao_correcoes: List[AcaoDeCorrecao]):
        values = []
        for regra in regras:
            (correto, erro) = ExecutarRegra.__aplicar_regras(regra=regra, values=conjunto_de_dados)
            values.append((correto, erro))
        print(values)
