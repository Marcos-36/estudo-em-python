#importtou a biblioteca ramdom
import random
#declarar variáveis
numero_secreto = random.randint (1,10)
tentativas = 0 
contagem_tentativas = 0
#introdução ao jogo
print("== Bem-vindo ao jogo de adivinhação ==")
print ("Tente adivinhar número secreto entre 1 e 10 ")
# laço de repetição / white = enquanto em portugol
while tentativas != numero_secreto:
    numero = int(input ("Digite um número : "))
    contagem_tentativas = contagem_tentativas + 1   
    if numero == numero_secreto :
        print (" você acertou, Parabens! ")
        print (f" E você precisou de {contagem_tentativas} tentativas.")
        break 
    elif numero < numero_secreto:
        print ('O número secreto é maior.')
    else:
        print("O número secreto é menor.")

   
