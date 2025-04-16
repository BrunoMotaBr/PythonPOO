class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print(f"{self.modelo} está ligado.")

    def desligar(self):
        print(f"{self.modelo} está desligado.")

    def exibir_dados(self):
        print(f"Modelo: {self.modelo}, Ano: {self.ano}")
