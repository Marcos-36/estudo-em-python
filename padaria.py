#declaração de variaveis
valor1 = 0 
valor2 = 0
valor3 = 0
valor4 = 0
valor5 = 0
pfrances = 0
pintegral = 0
pdoceliso = 0
pdocefarofa = 0
pforma = 0
opcao = 1
#laço de repetição
while opcao != 6:
    print("-- SEJAM MUITO BEM VINDOS A NOSSA PADARIA ❤️ --")
    print("|||||||||| PÃO & PROSA ❤️ 🍞 ||||||||||||||||")
    print("1️⃣  - Pão Francês 🍞")
    print("2️⃣  - Pão Integral 🍞")
    print("3️⃣  - Pão Doce Liso 🍞")
    print("4️⃣  - Pão Farofa 🍞")
    print("5️⃣  - Pão De Forma 🍞")
    print("6️⃣  - Fim Da Compra.")
    #escolha do usuario
    opcao = int(input("Escolha sua opção: "))
    #se opcao 1 pergunta a quantidade de pao e calculo com base na quantidade digitada
    if opcao == 1:
      pfrances = float(input("Digite a quantidade de pão francês que você deseja : "))
      valor1 = pfrances*1.04
      print(f"O valor de sua compra é : R${valor1:.2f}💰")
       #se nao opcao 2 pergunta a quantidade de pao e calculo com base na quantidade digitada
    elif opcao == 2:
        pintegral = float(input("Digite a quantidade de pão Integral que você deseja : "))
        valor2 = pintegral*1.04
        print(f"O valor de sua compra é : R${valor2:.2f}💰")
    #se nao opcao 3 pergunta a quantidade de pao e calculo com base na quantidade digitada
    elif opcao == 3:
        pdoceliso = float(input("Digite a quantidade de pão doce liso que você deseja : "))
        valor3 = pdoceliso*1.08 
        print(f"O valor de sua compra é : R${valor3:.2f}💰")
        #se nao opcao 4 pergunta a quantidade de pao e calculo com base na quantidade digitada
    elif opcao == 4:
        pdocefarofa = float(input("Digite a quantidade de pão doce farofa que você deseja : "))
        valor4 = pdocefarofa*1.11
        print(f"O valor de sua compra é : R$ {valor4:.2f}💰")
        #se nao opcao 5 pergunta a quantidade de pao e calculo com base na quantidade digitada
    elif opcao == 5: 
        pforma = float(input("Digite a quantidade de pão de forma que você deseja : "))
        valor5 = pforma*0.95
        print(f"O valor de sua compra é : R$ {valor5:.2f}💰")
        #se nao opcao 6 fim da compra e aprece para o cliente o recibo
    elif opcao == 6:
        #calculo do valor total
        valortotal = valor1 + valor2 + valor3 + valor4 + valor5 
        print("FIM DA COMPRA...")
        print("-------------------------------------")
        print("=== RECIBO DE SUA COMPRA ===")
        if pfrances > 0:
            print(f"Pão Francês : {pfrances:.0f}  unid - R$ {valor1:.2f}💸")
        if pintegral > 0:
            print(f"Pão Integral : {pintegral:.0f} unid - R$ {valor2:.2f}💰")
        if pdoceliso >0 :
            print(f"Pão doce liso :{pdoceliso:.0f} unid - R$ {valor3:.2f}🤑")
        if pdocefarofa >0 :
            print(f"Pão doce farofa : {pdocefarofa:.0f} unid - R$ {valor4:.2f}💵")
        if pforma > 0:
            print(f"Pão de forma :{pforma:.0f} unid - R$ {valor5:.2f}💷")
        print(f"TOTAL A PAGAR : R${valortotal:.2f}💴")
        print("=== AGRADECEMOS A PREFERÊNCIA ❤️ 🍞 ===")
        print("---------------------------------------")
        # para o laço
        break
    #caso digite uma opcao que nao esteja no menu informar o erromila 
    else:
        print("❌Opção inválida! Por favor, escolha uma opção válida do menu.")
