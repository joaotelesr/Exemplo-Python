import os
os.system("cls")

numero = int(input("Digite um número: "))

if numero > 0:
    print ("Seu número é positivo")

elif numero < 0:
    print ("Seu número é negativo")

elif numero == 0:
    print ("Seu número é neutro")