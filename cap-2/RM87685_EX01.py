print("\n***** Calculo de IMC *****\n")
print("\n*Para incluir o peso ou altura utilize '.' ao invés de ',' quando tiver casas decimais\n")
height = float(input("Digite sua altura: "))
weight = float(input("Digite seu peso: "))
result = (weight / (height ** 2))

if (result < 16.00):
    print("\nBaixo peso Grau III\n")
elif (result >= 16.00 and result <= 16.99):
    print("\nBaixo peso Grau II\n")
elif (result >= 17.00 and result <= 18.49):
    print("\nBaixo peso Grau I\n")
elif (result >= 18.50 and result <= 24.99):
    print("\nPeso ideal\n")
elif (result >= 25.00 and result <= 29.99):
    print("\nSobrepeso\n")
elif (result >= 30.00 and result <= 34.99):
    print("\nObesidade Grau I\n")
elif (result >= 35.00 and result <= 39.99):
    print("\nObesidade Grau II\n")
else:
    print("\nObesidade Grau III\n")
