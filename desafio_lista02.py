tabuada = range(1,11)

multiplicador = int(input('Insira um multiplicador:'))

print('Mostrando a tabuada do:', multiplicador)

for tabuada_5 in tabuada:
    resultado = tabuada_5 * multiplicador
    print (multiplicador,'X',tabuada_5, '=', resultado)

