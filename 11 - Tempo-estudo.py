import os
os.system ("cls")

nome = input("Digite seu nome:\n")
estudo = int(input("Digite quantas horas você estuda por dia:\n"))

if estudo < 2:
    print("Pouco estudo")
elif estudo >= 2 and estudo <= 4:
    print("Estudo médio")
elif estudo > 4:
    print("Muito estudo")

