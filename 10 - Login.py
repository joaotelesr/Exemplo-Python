import os
os.system ("cls")

usuario = input("Digite seu nome de usuário:\n")
senha = int(input("Digite sua senha:\n"))
if usuario == "admin" and senha == 123:
    print("Acesso Liberado")
else:
    print("Acesso Negado")