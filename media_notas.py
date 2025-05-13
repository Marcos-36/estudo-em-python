# pedir nota ao usuario 
notatrabalho = float (input("Digite a sua nota de trabalho : "))
notaprova = float (input("Digite a sua nota de prova : "))
#calcular media
media = (notatrabalho + notaprova)/2
print (f"A sua média e {media}")
if (media >=7) :
    print ("Parabéns, você esta aprovado!")
else :
    print ("Você esta reprovado! ")