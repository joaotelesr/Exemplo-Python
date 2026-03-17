import os
os.system("cls") 

#variaveis de entrada
nome = input("Digite o Nome do Produto:\n")
quantidade = int(input("\nDigite a Quantidade de Produtos:\n"))
preco = float(input("Agora Informe o Preço Unitário do Produto:\nR$"))
#total sem desconto
total = quantidade * preco

#Descontos
if quantidade <= 5:
    desconto = (quantidade * 2) / 100
elif quantidade > 5 and quantidade <=10:
    desconto = (quantidade * 3) / 100
elif quantidade > 10:
    desconto = (quantidade *5) / 100

totalapagar = total - desconto

print("O Preço Total do Produto é:\n", totalapagar)
      



