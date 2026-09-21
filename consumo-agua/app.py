# Solicita o tipo de imóvel
tipo = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()

# Solicita o consumo mensal de água
consumo = float(input("Digite o consumo mensal de água em m³: "))

# Classifica o consumo e exibe a mensagem correspondente
if tipo == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif (tipo == "apartamento" or tipo == "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
