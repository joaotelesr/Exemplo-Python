

print ("Seja Bem vindo a Calculadora de Média Virtual")

nome = input("Escreva seu Nome:\n")

valor01 = float(input("Digite o primeiro valor:\n"))
valor02 = float(input("Digite o segundo valor:\n"))
valor03 = float(input("Digite o terceiro valor:\n"))

total = (valor01 + valor02 + valor03) / 3

print(nome,"o seu resultado é:\n", total)

if(total>=7):
    print("Você foi Aprovado")

elif(total>=4 and total<=6):
   print("Você está de Recuperação")

else:
    print("Você foi Reprovado")