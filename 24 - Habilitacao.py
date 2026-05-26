import os
os.system("cls")

print("Exemplo Habilitação com While")

resposta = "sim"
while(resposta == "sim"):

    nome= input("Digite seu nome:\n")
    idade = int(input("\nDigite sua idade:\n"))

    if(idade >= 18):
        habilitacao = int(input("\nPossui Habilitação? (1-Sim ou 2-Não):\n"))

        if(habilitacao ==1):
            print("\nVocê pode dirigir!")
        else:
            print("\nVocê não possui Habilitação")

    else:
        print("\nVocê é menor de Idade!")

    resposta = input("\nVocê gostaria de executar novamente? (sim ou não):\n")

print("Fim do programa, espero ter ajudado!")

