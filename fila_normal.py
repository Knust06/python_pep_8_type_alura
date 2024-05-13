from fila_base import FilaBase
class FilaNormal(FilaBase):


    def gerasenhaatual(self) -> None:
        self.senhatual = f'NM{self.codigo}'

    def atualizafila(self) -> None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhatual)

    def chamacliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return (f'Cliente_atual: {cliente_atual}, dirija-se ao caixa: {caixa}')
