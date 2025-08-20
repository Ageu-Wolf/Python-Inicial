qtd_numeros = int(input('Quantidade de numeros:'))

lista = []
somatorio = 0

for i in range(1, qtd_numeros + 1):
    numero_digitado = int(input('Digite um numero:'))
    lista.append(numero_digitado)

print('Numeros digitados:')

for numero in lista:
    print(numero)
    somatorio += numero

print('A soma dos numeros é igual a:',somatorio)