import os

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2


while True:
    os.system("cls")

    print("Seja Bem Vindo a Super Calculadora 2.0 Pro Max")

    numero1 = int(input("Informe o Primeiro Número: "))
    numero2 = int(input("Informe o Segundo Número: "))

    print("\n[1] Somar\n[2] Subtrair\n[3] Multiplicar\n[4] Dividir")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"A soma é: {somar(numero1, numero2)}")
    elif opcao == 2:
        print(f"A subtração é: {subtrair(numero1, numero2)}")
    elif opcao == 3:
        print(f"A multiplicação é: {multiplicar(numero1, numero2)}")
    elif opcao == 4:
        print(f"A divisão é: {dividir(numero1, numero2)}")
    else:
        print("Operação inválida")

    # controle de reinício
    voltar = input("\nDeseja reiniciar o programa? (sim/nao): ").lower()

    if voltar == "sim":
        print("Pressione Enter para finalizar...")
        input()
        break
   
