from fila_base import FilaBase
from constantes import CODIGO_NORMAL


class FilaNormal(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senhatual = f'{CODIGO_NORMAL}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente_atual: {cliente_atual}, dirija-se ao caixa: {caixa}')
