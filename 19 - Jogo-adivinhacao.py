import os
os.system("cls")

import random

numero = random.randint(1, 10)

palpite = int(input("Digite um número de 1 a 10: "))

if palpite == numero:
    print("Você acertou!")
 
elif palpite > numero:
    print ("O seu palpite é maior que o número secreto!")
 
elif palpite < numero:
    print ("O seu palpite é menor que o número secreto!")
 

print(f"O número secreto foi:", numero)