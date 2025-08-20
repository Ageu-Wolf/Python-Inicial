var1 = 'Ageu'
var2 = 100
var3 = 'teste'

print(var1, var2,var3, 'continuação')

texto1 = 'Interpolando %s' % var1
print(texto1)

texto2 = 'Interpolando 2 %s ou %s' % (var1, var3)
print(texto2)

texto3 = 'Interpolando %s e %d' % (var3, var2)
print(texto3)

texto4 = 'Interpolando {a} e {b}'.format(a=var1, b=var2)
print(texto4)

texto5 = 'Interpolando {} e {}'.format(var1, var2)
print(texto5)

texto6 = f'Interpolando {var1} e {var2} e {var3}.'
print(texto6)