import os
import random

while True:
  os.system ("cls")

  print ("Bem vindo ao Sistema de Batalha do Pokemon")

  jogador_1 = 100
  jogador_2 = 100


  turno = "jogador"
  computador_fugiu = False
  eu_fugi = False
  erro = False

  while jogador_1 > 0 and jogador_2 > 0 and computador_fugiu == False and eu_fugi == False and erro == False:
     if turno == "jogador":
      print("\nSeu turno!")
    
      acao = input ("\nDIgite se você deseja: Ataque, Cura ou Fugir:\n").upper()

     if (acao == "ATAQUE"):
        jogador_2 -= 10
        print ("\nVocê Atacou.\n Vida do seu adversário: ", jogador_2)
    
    
     elif (acao == "CURA"):
        jogador_1 += 5
        print ("\nSua vida: ",jogador_1)
    
     elif (acao == "FUGIR"):
        print("\nVocê fugiu porque é ruim")
        eu_fugi = True
        break
     else:
        print ("\nDigite apenas uma das 3 opções")
        erro = True
        break
    
     turno = "inimigo"
    
       
     print ("\nTurno do Inimigo")
     input("pressione enter para continuar....\n\n\n")

     inimigo = random.choice(["Atacar", "Cura", "Fugir"])
     print(f"\n\nInimigo escolheu: {inimigo}")

     if (inimigo == "Atacar"):
        jogador_1 -= 10
        print(f"\n\nO inimigo te atacou!\nSua Vida:{jogador_1}")
    
     elif (inimigo == "Cura"):
        jogador_2 += 5
        print (f"\n\nO inimigo se curou!\nVida do inimigo:{jogador_2}")
    
     elif (inimigo == "Fugir"):
        print ("\n\nO inimigo fugiu")
        computador_fugiu = True
    
     turno = "jogador"

  print (f"Sua vida: {jogador_1}")
  print (f"Vida do inimigo: {jogador_2}")  
    
  if (jogador_1 > jogador_2):
        print("\nVocê ganhou!")

  elif (jogador_1 == jogador_2):
        print("Deu Empate!")

  else:
        print ("Você Perdeu!")
    
  jogar_novamente = input ("\nQuer jogar novamente? (SIM/NÃO):\n").upper()
    
  if (jogar_novamente == "sim"):
     break
  elif (jogar_novamente == "nao"):
     exit()
  
    