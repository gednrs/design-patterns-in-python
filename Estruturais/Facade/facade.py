class GerenciamentoEventos:

    def __init__(self) -> None:
        print('Gerenciamento de Enventos :: Vou organizar todos!')

    def organizar(self):
        self.salao = SalaoFestas()
        self.salao.agendar()

        self.florista = Florista()
        self.florista.arranjar_flores()

        self.comida = Restaurante()
        self.comida.preparar()

        self.musica = Banda()
        self.musica.montar_palco()

# Subsistema 1
class SalaoFestas:

    def __init__(self) -> None:
        print('SalaoFestas :: Agendando salão de festas')

    def esta_disponivel(self):
        print('SalaoFestas :: Está disponivel?')
        return True

    def agendar(self):
        if self.esta_disponivel():
            print('SalaoFestas :: Agendamento realizado')

# Subsistema 2
class Florista:
    def __init__(self) -> None:
        print('Florista :: Flores para o evento?')

    def arranjar_flores(self):
        print('Florista :: Rosas e Margaridas serão usadas')
    

# Subsistema 3
class Restaurante:

    def __init__(self) -> None:
        print('Restaurante :: Comida para o envento')
    
    def preparar(self):
        print('Restaurante :: Comida chinesa e brasileira')

# Subsistema 4
class Banda:

    def __init__(self) -> None:
        print('Banda :: Arranjo das musicas para o evento')
    
    def montar_palco(self):
        print('Banda :: Preparando o palco')


# Cliente
class Cliente:

    def __init__(self) -> None:
        print('Cliente :: Preparação para o casamemto')

    def contrata_gerente_eventos(self):
        print('Cliente :: Contratando empresa eventos')
        ge = GerenciamentoEventos()
        ge.organizar()

    def __del__(self):
        print('Muito bom organizar este evento')


if __name__ == '__main__':
    cliente = Cliente()
    cliente.contrata_gerente_eventos()