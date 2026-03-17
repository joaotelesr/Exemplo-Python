import os
os.system ("cls")

nome = input ("Escreva o nome do professor:\n")
nivel = int (input ("Digite o número do nível do profissional:\n"))
aulas = int (input ("Digite quantas aulas semanais:\n"))

total = 0
if nivel == 1:
    total = (aulas * 4) * 12

elif nivel == 2:
    total = (aulas * 4) * 17

elif nivel == 3:
    total = (aulas * 4) * 25

else:
    print("Nível não indentificado, porfavor digite um número de 1 a 3")
    total=0

print ("Salário total bruto:\n", total)