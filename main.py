from Chevrolet import Chevrolet
from Fiat import Fiat

def main():
    carro1 = Chevrolet("Onix", 2020)
    carro2 = Fiat("Uno", 2016)

    carro1.ligar()
    carro1.exibir_dados()

    print()

    carro2.ligar()
    carro2.exibir_dados()

if __name__ == "__main__":
    main()
