import os
os.system ("cls")

nome = input("Digite seu nome:\n")
peso = float(input("Digite seu peso em quilograma:\n"))
altura = float(input("Digite sua altura em mentros:\n"))

total = peso / (altura * altura)

if total <= 16.9:
    print ("Você está muito abaixo do peso")
elif total >= 17 and total <= 18.4:
    print ("Você está abaixo do peso")
elif total >= 18.5 and total <= 24.9:
    print("Você está no peso normal")
elif total >= 25 and total <= 29.9:
    print ("Você está acima do peso")
elif total >=30 and total <=34.9:
    print ("Obesidade grau 1")
elif total >=35 and total <=40:
    print ("Obesidade grau 2")
elif total > 40:
    print ("Obesidade grau 3")

