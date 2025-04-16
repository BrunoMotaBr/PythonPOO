from Carro import Carro

class Fiat(Carro):
    def __init__(self, modelo, ano):
        super().__init__(modelo, ano)
        self.marca = "Fiat"

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Marca: {self.marca}")
