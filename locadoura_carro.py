print("|||||||||||||||||||||||||||||||||")
print("🚗  LOCADORA CARROS NOVOS 🚗 ")
print("|||||||||||||||||||||||||||||||||")
print("---------------------------------------")
# tabela de preços
print("     TABELA DE PREÇOS")
print("📌 A cada KM rodado: R$ 0,20 ")
print("📌 A cada dia alugado: R$ 90 ")
print("-----------------------------------------")

# entrada de dados
dia = float(input("📆 Digite quantos dias o carro foi alugado: "))
km = float(input(" Digite quantos KMs você percorreu com o carro: "))

# cálculos com base na entrada do usuário
totaldia = dia * 90
totalkm = km * 0.20
total = totaldia + totalkm

# recibo no final
print("-----------------------------------")
print("🧾 ===    RECIBO A PAGAR   === 💰")
print(f"📅 Valor dos dias alugados: R$ {totaldia:.2f}")
print(f"🛣 Valor dos KMs percorridos: R$ {totalkm:.2f}")
print(f"💸 Valor total a pagar: R$ {total:.2f}")
print("------------------------------------")