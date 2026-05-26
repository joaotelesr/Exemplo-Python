import os
os.system("cls")

numero = int(input("Digite um número:"))
valor = int(input("Digite o limite da sua tabuada:"))

contador = 0

while(contador <= valor):
    print(f"{numero} x {contador} = {numero * contador}")
    contador+=1