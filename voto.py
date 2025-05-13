anoatual = 2025
anonascimneto = int (input("Digite o ano de seu nascimento :"))
idade = anoatual - anonascimneto
print(f"Você tem {idade} anos. ")
if idade < 16:
    print ("Você não pode votar !")
elif idade < 18 or idade > 70:
    print ("Seu voto é opcional.")
else: 
    print ("Seu voto é obrigatório.")