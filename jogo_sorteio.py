from random import randint

numero_sorteado = randint(1, 5)
numero_apostado = int(input('infrome um numero entre 1 e 5:'))

if numero_apostado == numero_sorteado:
    print('Você Acertou')
else:
    print('Você Errou')

print('numero_sorteado:', numero_sorteado)
print('Numero Apostado:', numero_apostado)