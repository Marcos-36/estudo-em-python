print("🌡||||||||||||||||||||||||||||||||")
print("🌡 MENU DE CONVERSÃO DE TEMPERATURA ")
print("🌡||||||||||||||||||||||||||||||||")
# laço de repetição 
opcao = -1
while opcao != 0:
   # menu
   print("📋 Você deseja:")
   print("1️⃣ - Converter Celsius para Fahrenheit 🌡℉")
   print("2️⃣ - Converter Celsius para Kelvin 🌡")
   print("0️⃣ - Para Sair ❌")
   opcao = int(input("👉 Escolha uma opção: "))
   
   # opção 1: Celsius -> Fahrenheit
   if opcao == 1:
     celsius = float(input("🌡 Digite a temperatura em Celsius: ")) 
     tempinicial = (celsius * 9/5) + 32
     print("✅ A temperatura em Fahrenheit é:", tempinicial, "°F 🔥")
     print("👋 Encerrando...")
     print("||||||||||||||||||||||||||||||||||||||")
     break
   
   # opção 2: Celsius -> Kelvin
   elif opcao == 2:
      celsius = float(input("🌡 Digite a temperatura em Celsius: ")) 
      tempinicial = celsius + 273.15
      print("✅ A temperatura em Kelvin é:", tempinicial, "K ❄")
      print("👋 Encerrando...")
      print("||||||||||||||||||||||||||||||||||||||")
      break
   
   # opção 0 sair
   elif opcao == 0:
     print("============================")
     print("👋 Encerrando ... Até logo!")
     print("============================")
     break
   
   # opção inválida
   else:
      print("❌ Opção inválida! Por favor, escolha uma opção válida do menu.")