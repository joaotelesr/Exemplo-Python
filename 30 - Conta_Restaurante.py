import os
os.system("cls")

def calculo (conta, pessoa):
    return conta / pessoa

print ("Seja bem vindo ao App Minha Conta!")
conta = int(input("Informe o valor da conta:\nR$"))
pessoa = int(input("Informe a quantidade de pessoas:\n"))
print("Pressione Enter para calcular...")
input()
print (f"Total da conta: {conta}\nNúmero de Pessoas: {pessoa}\nValor por pessoa: {calculo(conta, pessoa)}")