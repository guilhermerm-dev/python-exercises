def caculateAndPrintBonusPayment(signatureType, annualBilling):
    if(signatureType.lower() == "basic"):
        print("Valor a ser pago: ", annualBilling * 0.30)
    elif(signatureType.lower() == "silver"):
        print("Valor a ser pago: ", annualBilling * 0.20)
    elif(signatureType.lower() == "gold"):
        print("Valor a ser pago: ", annualBilling * 0.10)
    elif(signatureType.lower() == "platinum"):
        print("Valor a ser pago: ", annualBilling * 0.05)
    else:
        return

print("\n***** Calculo de Bônus Por assinatura *****\n")
print("\n*Para números com casas decimais use '.' ao invés de ','\n")
signatureType = input("Tipo de assinatura: ")
annualBilling = float(input("Faturamento anual: "))

caculateAndPrintBonusPayment(signatureType, annualBilling)