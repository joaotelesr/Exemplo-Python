import os
os.system("cls")

saldo= 10000

print("Seja bem-vindo ao seu caixa eletronico")

#lobby principal 
while True:
    print("\nMenu de operação ")
    print("1- Ver o saldo")
    print("2- Depositar")
    print("3- Sacar o dinehrio")
    print("4- Sair do banco")
    break
opção= input("Escolha a sua opção: ")

if opção== "1":
    print(f"saldo atual:R$ {saldo}")

elif opção=="2":
    valor= float(input("Valor do deposito:\nR$ "))
    saldo+=valor 
    print(f"Seu deposto foi realizado\nSaldo atual:\n{valor}")

elif opção== "3":
        valor = float(input("Valor do saque:\nR$"))
        if valor <= saldo:
            saque = saldo - valor
            print(f"Saque realizado!\nSaldo Atual\n{saque}")
        else:
            print("Erro: Saldo insuficiente!")

elif opção== "4":
        print("Encerrando sistema...")

# Sai do loop while

else:
    print("Opção inválida!")
    input("\nPrecione a tecla Enter para continuar")