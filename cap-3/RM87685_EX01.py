print("\n***** Ingestão de Calorias *****\n")
print("Insira a quantidade de refeições que foram feitas no seu dia hoje\n")
mealsCount = int(input("Quantidade: "))
caloriesSum = 0
for i in range(mealsCount):
    caloriesSum += float(input(f"Quantidade de calorias que foram ingeridas na refeição n{i + 1}: " ))
    
print(f"\nO total de calorias ingeridas no dia de hoje foi: {caloriesSum}")
