import os
os.system("cls")
estoque = int(input("Digite o valor dos produtos no estoque:\n"))
if estoque <=5:
    print("Estoque Baixo")
else:
    print("Estoque OK")