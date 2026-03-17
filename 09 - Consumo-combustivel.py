import os
os.system ("cls")

km = float(input("Digite quantos quilometros foram percorridos(KM):\n "))
combustivel = float(input("\nDigite o gasto de combustível em Litros:\n"))

media = km / combustivel
print ("\nSeu consumo médio do veículo em km por litro foi:\n", media)