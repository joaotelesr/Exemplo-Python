import os
os.system("cls")

print("Manipulando Listas ou Arrays")

#Exemplo d criação e lístas
numeros = [1,2,3,4,5]
nomes = ["Joaquim", "Maria", "Ana"]

print("Listas Iniciais")
print(nomes)
print("=====================================")
print(f"\nNome da posição 1 da lista é: {nomes[1]}")
print("=====================================")

#Alterando o nome da posição 1
nomes[1] = "Ricardo"
print(f"\nLista nova: {nomes}")
print("=====================================")

#Adicionando um elemento no final da lista
nome = input ("\nDigite um nome:")
nomes.append(nome)
print(nomes)
print("=====================================")

#adicionando um elemento em uma pos. especifica
nomes.insert(2, "Michael Jackson")
print("\nLista Atualizada")
print(nomes)
print("=====================================")

#Removendo o elemento da posição 3 ()
del nomes[3]
print("\nLista atualizada")
print(nomes)
print("=====================================")