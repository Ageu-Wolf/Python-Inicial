from cmath import e


texto = 'este é o meu texto'
texto2 = 'OUTRO TEXTO'

print (texto.upper())
print(texto2.lower())
print(texto2.title())

print(texto.replace('e','a'))
# 'e' Será substituido e 'a' irá substituir

texto3 = 'A Rita é minha namorada'

print(texto3)
print(texto3.replace('Rita','João').replace('A','O').replace('minha','meu').replace('namorada','namorado'))

texto4 =  'Hoje a aula foi muito produtiva'
print(texto4)
print(texto4.replace('i','1').replace('b','3').replace('o','0').replace('a','4'))

variavel = 'GREMISTA'
tamanho = len(variavel)
print(tamanho)
#len calcula quantos caracteres tem na frase/dentro da variavel
