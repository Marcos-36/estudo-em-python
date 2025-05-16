#bonus de venda
#entrada de dados
print("=============================")
print("Bem vindo ao desafio do mês💰")
print("Que vença o melhor")
print("=============================")
nome = input("Digite o seu nome : ")
salario = float (input("Qual o valor do seu salário fixo ? "))
vendas = int (input("Qual foi o total de suas vendas ? "))
#se o fucionario bater a meta que e acima de 20 bonus obtido
if vendas >= 20:
    #calculo de bonus
    bonus = salario*0.15
    salariofinal = salario + bonus
    #mostra o fucionario que conseguiu o bonus e resultado do novo salario
    print ("Meta atingida!😎")
    print(f"Nome:{nome}")
    print(f"Salário fixo: R$ {salario:.2f}🤑")
    print(f"Comissão: R$ {bonus:.2f}🤑")
    print(f"Salário total : R$ {salariofinal:.2f}💰")
    #se não conseguiu mostra que não foi dessa vez que ele conseguiu
else:
    print("Meta não foi atingida.😭")
    print(f"Nome:{nome}")
    print(f"Salário fixo: R$ {salario:.2f}")