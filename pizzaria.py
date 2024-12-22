class Ingrediente:
    def __init__ (self, nome: str, preço: int) -> None:
        self.nome = nome
        self.preço = preço

class Pizza:
    def __init__ (self, nome: str, tamanho: str, massa: str) -> None:
        self.nome = nome
        self.tamanho = tamanho
        self.massa = massa
        self.lista_ingredientes = []
        self.preço_final = 0

    def exibir_detalhes(self) -> str:
        print(f'Pizza {self.nome}, Tamanho {self.tamanho}, Massa {self.massa}, R$ {self.preço_final}')

    def adicionar_ingrediente(self, ingrediente: Ingrediente):
        itens = [ingrediente.nome, ingrediente.preço]
        self.lista_ingredientes.append(itens)

    def preço(self) -> float:
        soma = 0
        for lista in self.lista_ingredientes:
            for item in lista:
                if type(item) == int:
                    soma += item
        if self.tamanho == 'P':
            tam = 1

        elif self.tamanho == 'M':
            tam = 1.5
        
        else:
            tam = 1.75

        self.preço_final = soma * tam

class Local(Pizza):
    def __init__ (self, nome: str, tamanho: str, massa: str, mesa: int):
        super().__init__(nome, tamanho, massa)
        self.mesa = mesa

    def entregar(self):
        print(f'Servido na mesa {self.mesa}')

class Endereço(Pizza):
    def __init__ (self,  nome: str, tamanho: str, massa: str, endereço: str):
        super().__init__(nome, tamanho, massa)
        self.endereço = endereço

    def entregar(self):
        print(f'Enviado para o endereço {self.endereço}')

        

pizza1 = Pizza('Margherita', 'M', 'Tradicional')
pizza2 = Pizza('Vegetariana', 'G', 'Integral')

pizza1.adicionar_ingrediente(Ingrediente('manjericão', 3))
pizza1.adicionar_ingrediente(Ingrediente('tomate', 5))
pizza1.adicionar_ingrediente(Ingrediente('queijo vegetal', 15))

pizza2.adicionar_ingrediente(Ingrediente('Beringela', 4))
pizza2.adicionar_ingrediente(Ingrediente('Azeitona', 7))
pizza2.adicionar_ingrediente(Ingrediente('Tomate seco', 10))
pizza2.adicionar_ingrediente(Ingrediente('Queijo vegetal', 15))
pizza1.preço()
pizza2.preço()

pizza1.exibir_detalhes()
pizza1 = Local('Margherita', 'M', 'Tradicional', 4)
pizza1.entregar()

pizza2.exibir_detalhes()
pizza2 = Endereço('Vegetariana', 'G', 'Integral', 'Rua dos Bobos, n° 0')
pizza2.entregar()