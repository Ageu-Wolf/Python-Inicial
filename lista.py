lista1 = ['Uva','Melancia','Limão']

print(lista1)

print(lista1[1])
print(lista1[-1])
print(lista1[0:2])
print(lista1[1:3])
print(lista1[0], lista1[2])
print(len(lista1))
#Len em uma lista, conta quantas letras ou numeros existem dentro dela

lista1.append('Banana')

print(lista1)

'''Este é um comentário
com mais de 1linha
linha 3
linha 4'''

elemento_removido = lista1.pop()
print(elemento_removido)
print(lista1)
lista1.pop(1)
print(lista1)
