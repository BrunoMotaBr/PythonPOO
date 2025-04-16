from Carro import Carro

class Chevrolet(Carro):
    def __init__(self, modelo, ano):
        super().__init__(modelo, ano)
        self.marca = "Chevrolet"

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Marca: {self.marca}")
