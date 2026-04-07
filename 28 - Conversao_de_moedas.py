import funcoes_conversor_moedas as funcoes


#Criando a função main - Principal
def main():
    funcoes.limpar_tela()
    #Chamar a função exibir menu
    funcoes.exibir_menu()
    #Solicitando a opção do usuário
    opcao = int(input("Escolha uma opção:"))

    if(opcao == 1):
        quantia_dolar = float(input("informe a quantia de dolares:"))
        cotacao = float(input("Informe a cotação:").replace(",","."))
        resultado = funcoes.converter_dolar_para_real(quantia_dolar, cotacao)
        print(f"O total da conversão é: R${resultado}")
    
    elif(opcao == 2):
        quantia_real = float(input("Informe a quantia de reais:"))
        cotacao = float(input("informe a cotação:").replace(",","."))
        resultado = funcoes.converter_real_para_dolar(quantia_real, cotacao)
        print(f"O total da conversão é: US${resultado}")
    
    elif(opcao == 3):
        funcoes.sair()
    
    
    

#Chamando a função principal do programa
main()