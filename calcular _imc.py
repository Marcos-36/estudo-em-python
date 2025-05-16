print("========================================")
print("  Bem-vindo à Calculadora de IMC! 🧮💪")
print("========================================")

# Entrada de dados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibição do IMC
print(f"\nSeu IMC é: {imc:.2f} 📊")

# Classificação com base no IMC
print("Classificação:", end=" ")

if imc < 18.5:
    print("Abaixo do peso 🥶")
elif 18.5 <= imc <= 24.9:
    print("Peso normal ✅")
elif 25.0 <= imc <= 29.9:
    print("Sobrepeso ⚠")
else:
    print("Obesidade 🚨")