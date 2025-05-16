#calculadora
#while laço de repetição
opcao = -1
while opcao != 0:
    #menu
    print("-----------------------")
    print("==== CALCULADORA ====")
    print("1- Somar")
    print("2- Subtrair")
    print("3- Multiplicar")
    print("4- Dividir")
    print("0- Sair")
    print("----------------------")
    #escolha do usuario
    opcao = int (input("Escolha uma opção :"))
    #pedir ao usuario para digita dois numeros caso ele digite de 1 a 4 
    if opcao >= 1 and opcao <= 4:
        numero1 = float (input("Digite o primeiro número: "))
        numero2 = float (input("Digite o segundo número: "))
        #opção 1 somar e calculo
    if opcao == 1:
        resultado = numero1 + numero2
        print(f"O resultado da somar é: {resultado:.0f}")
        #opção 2 subtração e calculo
    elif opcao == 2:
        resultado = numero1 - numero2
        print(f"O resultado da subtração é: {resultado:.0f}")
        #opção 3 multiplicação e calculo
    elif opcao == 3:
        resultado = numero1 * numero2
        print(f"O resultado da multiplicação é: {resultado:.2f}")
        #opção 4 divisão e calculo
    elif opcao == 4:
        if numero2 != 0: 
            resultado = numero1 / numero2
            print(f"O resultado da divisão é: {resultado:.2f}")
            #mostra ao usuario que não e possivel divisão com zero
        else:
            print("Erro: Divisão por zero não é permitida!")
    #opção 0 encerra
    elif opcao == 0:
        print("=== Encerrando a calculadora... ===")
        break
    #caso digite um número diferente do menu mostra opção invalida
    else:
        print("Opção inválida! Por favor, escolha uma opção válida do menu.")
     
 