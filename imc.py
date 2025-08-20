
print('Cálculo do IMC')


peso = float(input('Informe o seu peso em KG:'))
altura = float(input('informe a sua altura em metro:'))


resultado = peso / (altura * altura)
print('IMC:', round(resultado,1))

if resultado < (18.5):
    print('Abaixo do peso')

elif resultado >= 18.5 and resultado <=24.9:
    print('Peso Normal')
elif resultado >= 25 and resultado <=29.9:
    print('Sobrepeso')
elif resultado >= 30 and resultado <= 34.9:
    print('Obesidade Grau 1')
elif resultado >= 35 and resultado <=39.9:
    print('Obesidade Grau 2')
else:
    print('Obesidade grau 3 ou mórbida')

