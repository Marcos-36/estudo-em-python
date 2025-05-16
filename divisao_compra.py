#divisão de compra
print("==========================================")
print("Seja bem vindo cliente ")
#entrada de dados
valor = float (input("Digite o valor de sua compra : "))
divisao = int(input("Digite de quanto que dividir : "))
#calculo da compra
prestacao = valor/divisao
#resultado final
print(f"Valor total de sua compra:R${valor:.2f}🤑") 
print(f"Valor de cada uma das {divisao} prestações e:R${prestacao:.2f}💰")
print("==========================================")