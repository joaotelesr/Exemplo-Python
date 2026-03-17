import os
os.system("cls")
veiculo = input("Digite o tipo de veículo:\n")
if veiculo == "carro":
    print("O valor do seu pedágio é de R$10")
elif veiculo == "moto":
    print("O valor do seu pedágio é de R$5")
elif veiculo == "caminhão":
    print("O valor do seu pedágio é de R$20")
else:
    print("Tipo inválido")