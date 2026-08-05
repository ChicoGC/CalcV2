def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))

imc = calcular_imc(peso, altura)

if imc <= 18.5:
   print ('2-3 years dagestan and forget' )

if imc > 18.6:
   print (f'meh, seu mc é {imc:.2f}' )

#ps:eu nao sei oq eu to fazendo da minha vida, esse codigo é um fracasso.
