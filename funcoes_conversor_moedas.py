import os

#Criando as funções
#Criando a função que exibi o menu
def exibir_menu():
    print("=== Conversor de Moedas ===")
    print("[1] - Converter DOLAR -> REAL")
    print("[2] - Converter REAL -> DOLAR")
    print("[3] - Sair")
#Limpar terminal
def limpar_tela():
    os.system("cls")

#Criando  Função que converte dolar para real
def converter_dolar_para_real(quantia_dolar,cotacao):
    total_reais = quantia_dolar * cotacao
    return total_reais

#Converter de real para dolar
def converter_real_para_dolar(quantia_real, cotacao):
    total_dolares = quantia_real / cotacao
    return total_dolares

#Função sair
def sair():
    exit()