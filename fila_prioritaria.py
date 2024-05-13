from typing import Dict, Union, List

from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente_atual: {cliente_atual}, dirija-se ao caixa: {caixa}'

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {}
        if flag != 'detail':
            estatistica[f'{agencia}-{dia}'] = len(self.clientes_atendidos)
        else:
            estatistica['agencia'] = agencia
            estatistica['dia'] = dia
            estatistica['clientes_atendidos'] = self.clientes_atendidos
            estatistica['quantidade_clientes_atendidos'] = (
                len(self.clientes_atendidos)
            )

        return estatistica
