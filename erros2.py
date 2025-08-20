from distutils.log import error
from logging import exception


def entrar_inteiro():
    solicitar_inteiro = True
    while solicitar_inteiro:
        try:
            numero = int(input('Número: '))
            if numero < 10 or numero > 20:
                raise Exception('Valor digitado fora do range!')
            return numero
        except exception as erro:
            print(erro)
            print('Você deve digitar um número!')


nr1 = entrar_inteiro()
nr2 = entrar_inteiro()

print(f'Resultado da soma: {nr1 + nr2}')