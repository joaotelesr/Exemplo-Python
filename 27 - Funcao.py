import os 
os.system("cls")

#Criando a primeira função
def escreva():
    print("Olá Mundo")

#Chamando a Função
escreva()

#Criando uma função com parametro
def exibir_dados(nome,idade,email):
    print(f"Nome:{nome}")
    print(F"Idade:{idade}")
    print(f"Email:{email}")
    print("=" * 100)

#Chamando a função exibir dados
exibir_dados("João",16,"joaoteles@gmail.com")
exibir_dados("lavinia",16,"lavinia@gmail.com")

#Criando uma função com retorno
def somar(num1,num2):
    resultado = num1 + num2
    return resultado

#Chamando função com retorno
total = somar(10,20)
print (f"O total será {somar(10,20)}")