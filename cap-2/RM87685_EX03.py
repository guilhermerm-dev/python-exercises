def getMaxVotedDayValue(dictionary, key):
    return dictionary[key]

print("\n***** Calculo de Votos *****\n")
monday = int(input("Digite a quantidade de votos para segunda-feira: "))
tuesday = int(input("Digite a quantidade de votos para terça-feira: "))
wednesday = int(input("Digite a quantidade de votos para quarta-feira: "))
thursday = int(input("Digite a quantidade de votos para quinta-feira: "))
friday = int(input("Digite a quantidade de votos para sexta-feira: "))

daysVotesDictionary = {
    "segunda-feira": monday,
    "terça-feira": tuesday,
    "quarta-feira": wednesday,
    "quinta-feira": thursday,
    "sexta-feira": friday
}

max_voted_day_key = max(daysVotesDictionary, key=daysVotesDictionary.get)
print("O dia mais votado foi: ", max_voted_day_key, getMaxVotedDayValue(daysVotesDictionary, max_voted_day_key))

