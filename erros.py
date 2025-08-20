
try:
    n1 = int(input('numero 1:'))
    n2 = int(input('numero 2:'))
    n3 = int(input('numero 3:'))

    r = (n1+n2) / n3
    print(r)

except ValueError:
    print('Voce deve digitar apenas numeros inteiros!')
    r = 0
except ZeroDivisionError:
    print('O terceiro número deve ser maior que zero!')
except Exception as erro:

    print('Ops! Tem algo errado. Erro:', erro)

