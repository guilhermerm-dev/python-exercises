import sys


def fibonacci(number):
    numberOne = 0
    numberTwo = 1
    for i in range(number + 1):
        if(number == numberTwo):
            return bool(True)
        num = numberTwo + numberOne
        numberOne = numberTwo
        numberTwo = num
    return bool(False)


print("\n***** Fibonacci *****\n")
print("Procure um número na sequência de fibonacci\n")
searchedNumber = int(input("Número: "))
if(fibonacci(searchedNumber)):
    print("Ação bem sucedida!")
else:
    print("A ação falhou...")
