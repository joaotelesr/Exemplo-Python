import os
os.system ("cls")

velocidade = int(input("Digite a velocidade em KM:\n"))

if velocidade >= 80:
    print ("Multado!")
else:
    print ("Dentro do limite")