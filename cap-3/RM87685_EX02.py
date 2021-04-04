print("\n***** Transações financeiras *****\n")
print("Insira a quantidade de transações que foram feitas no dia hoje\n")
transactionsCount = int(input("Quantidade: "))
transactionsSum = 0
for i in range(transactionsCount):
    transactionsSum += float(input(f"\nValor da transação n{i + 1}: " ))

averageTransactionsSum = (transactionsSum / transactionsCount)
print(f"\nO total das transações de hoje é: {transactionsSum}")
print(f"\nA média das transações é: {averageTransactionsSum}\n")

