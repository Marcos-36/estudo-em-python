opcao = 0
while opcao != 5:
    print("-------------")
    print("CARDÁPIO")
    print("1- Hamburguer")
    print("2- Pizza")
    print("3- Salada")
    print("4- Refrigerante")
    print("5- sair")
    print("-----------------")
    opcao = int (input("Escolha uma opção : "))
    if opcao == 1:
        print("Você escolheu hamburguer.")
    elif opcao == 2:
        print("Você escolheu pizza.")
    elif opcao == 3:
        print ("Você escolheu salada.")
    elif opcao == 4:
        print ("Você escolheu refrigerante.")
    elif opcao == 5:
        print("Saindo do Cardápio... , Agradecemos a preferência.")
        break
    else :
        print("Opção inválida. tente novamente")
        