import os

# =========================
# Pior filme
# =========================
def pior_filme(filmes):
    return min(filmes,key=lambda item: item["media"])
# =========================
# Melhor filme
# =========================
def melhor_filme(filmes):
    return max(filmes, key=lambda item: item["media"])
# =========================
# Devolver Filme
# =========================
def devolver_filme(filmes):
    os.system("cls")
    print("=== Devolução de Filme ===")
    titulo = input("Informe o nome do filme: ")
    for item in filmes:
        if item["titulo"].lower() == titulo.lower():
            if not item["Disponível"]:
                print (f"O filme estava com: {item['cliente']}")

                nota = float(input("De uma nota de 0 a 10: "))  
                item["avaliacoes"].append(nota)
                item["media"] = calcular_media(item["avaliacoes"])
                item["classificacao"] = classificar_filme (item["media"])
                item["cliente"] = None
                item["Disponível"] = True
                print("Filme Devolvido com sucesso!")
                print(f"A nova média do filme é: {item['media']}")
                input("Pressione <enter> para continuar...")
            else:
                print("Esse filme está Disponível") 
        
# =========================
# Alugar filme
# =========================
def alugar_filmes(filmes):
    os.system("cls")
    print("=== Alugueis de Filme ===")
    titulo = input("Informe o nome do filme: ")
    for item in filmes:
        if item["titulo"].lower() == titulo.lower():
            #filme existe
            if item["Disponível"] == True:
                nome = input("Informe seu nome: ")
                item["Disponível"] = False
                item["cliente"] = nome

                print("Filme alugado com Sucesso!")
            else:
                print(f"O filme está alugado pelo cliente {item['cliente']}")
        

    input("Pressione <enter> para continuar...")
        


# =========================
# Classificar filme
# =========================
def classificar_filme(media):
    if(media >= 8):
        return "Regular"
    elif(media >= 5):
        return "Regular"
    else:
        return "Flop"

# =========================
# Calcular a média
# =========================
def calcular_media(avaliacoes):
    if len(avaliacoes) == 0:
        return 0
    return round(sum(avaliacoes) / len(avaliacoes),1)

# =========================
# Buscar Filme
# =========================
def buscar_filme(titulo, filmes):
    filme_encontrado =""
    for item in filmes:
        if item["titulo"].lower() == titulo.lower():
            return item
        
    return filme_encontrado

# =========================
# Menu do CLiente
# =========================
def carregar_menu_cliente():
    os.system("cls")
    while True:
        print("=== MENU Cliente ===")
        print("[1] - Ver Catálogo")
        print("[2] - Buscar Filme")
        print("[3] - Alugar Filme")
        print("[4] - Devolver Filme")
        print("[5] - Voltar")

        op = int(input("Escolha uma opção:"))

        if (op == 1):
            os.system("cls")
            exibir_catalogo(filmes)
            input("Pressione <Enter> para continuar")
        
        elif(op == 2):
            os.system("cls")
            print("=== Encontre um Filme ===")
            titulo = input("Digite o nome do filme:")
            filme = buscar_filme(titulo, filmes)

            if filme:
                print(f"Filme encontrado: {filme}")
            else:
                print("Filme não encontrado")
            input("Pressione <Enter> para continuar")
        
        elif(op == 3):
            alugar_filmes(filmes)
        
        elif(op == 4):
            devolver_filme(filmes)
        elif(op == 5):
            return

# =========================
# Exibir Catálogo de Filmes
# =========================
def exibir_catalogo(filmes):
    os.system("cls")
    print("=== Catálogo de Filmes ===")

    for item in filmes:
        print(f"Título: {item["titulo"]}")
        print(f"Gênero: {item["genero"]}")
        print(f"Classificação: {item["classificacao"]}")
        print(f"Avaliações: {len(item["avaliacoes"])}")
        
        if(item["Disponível"] == True):
            status = "Disponível"
        else:
            status = f"Alugado por {item["cliente"]}"
        
        print(f"Status: {status}")
        print("-" * 30)

# =========================
# Cadastrar Filme
# =========================
def cadastrar_filme():
    os.system("cls")
    titulo = input("Título do filme:")
    genero = input("Gênero: ")

    filme = {
        "titulo" : titulo,
        "genero" : genero,
        "avaliacoes" : [],
        "media" : 0,
        "classificacao" : "Sem avaliações",
        "Disponível": True,
        "cliente": None 
    }
    os.system("cls")
    return filme

# =========================
# Menu Administrador
# =========================
def carregar_menu_admin():
    os.system("cls")
    senha = input("Informe a senha do admin:")
    os.system("cls")
    if(senha != "123"):
        print("Acesso negado!")
        return
    
    while True:
        os.system("cls")
        print("=== Menu ADMIN ===")
        print("[1] - Cadastrar Filme")
        print("[2] - Ver catálogo")
        print("[3] - Top e Flop")
        print("[4] - Voltar")
        
        op = int(input("Esoclha uma opção: "))
        if(op == 1):
            os.system("cls")
            print("Cadastro de Filmes")
            filme = cadastrar_filme()
            filmes.append(filme)
            print("Filme cadastrado!")
            input("Pressione <Enter> para continuar")

        elif(op == 2):
            os.system("cls")
            exibir_catalogo(filmes)
            input("Pressione <Enter> para continuar")
        
        elif(op == 3):
            print("=== Filmes Top e Flop ===")
            print(f"Melhor Filme: {melhor_filme(filmes)}")
            print(f"Pior Filme: {pior_filme(filmes)}")
            input("Pressione <enter> para continuar...")

        elif(op == 4):
            break 
    
# =========================
# Sistema Principal
# =========================
os.system("cls")

# Lista de filmes
filmes = []

filmes.append({
    "titulo": "Interestelar",
    "genero": "Ficção Científica",
    "avaliacoes": [],
    "media": 0,
    "classificacao": "Sem avaliações",
    "Disponível": True,
    "cliente": None
})

filmes.append({
    "titulo": "O Poderoso Chefão",
    "genero": "Crime",
    "avaliacoes": [],
    "media": 0,
    "classificacao": "Sem avaliações",
    "Disponível": True,
    "cliente": None
})

filmes.append({
    "titulo": "Vingadores: Ultimato",
    "genero": "Ação",
    "avaliacoes": [],
    "media": 0,
    "classificacao": "Sem avaliações",
    "Disponível": True,
    "cliente": None
})

filmes.append({
    "titulo": "Toy Story",
    "genero": "Animação",
    "avaliacoes": [],
    "media": 0,
    "classificacao": "Sem avaliações",
    "Disponível": True,
    "cliente": None
})

filmes.append({
    "titulo": "Parasita",
    "genero": "Drama",
    "avaliacoes": [],
    "media": 0,
    "classificacao": "Sem avaliações",
    "Disponível": True,
    "cliente": None
})

while True:
    os.system("cls")
    print("=== Bem vindo a locadora do Sesi ===")
    print("[1] - Entrar como Cliente")
    print("[2] - Entrar como Administrador")
    print("[3] - Sair")

    op = int(input("Escolha uma opção: "))
    
    #Verificar qual foi a opção escolhida
    if(op == 1):
        #Entrou como Cliente
        print("Entrou como Cliente")
        carregar_menu_cliente()
    
    elif(op == 2):
        #Entrou como Administador
        print("Entrou como Administrador")
        carregar_menu_admin()
    
    elif(op == 3):
        #Escolheu sair
        print("Obrigado por utilizar o sistema...")
        input("Pressione <enter> para sair")
        break