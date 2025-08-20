print('LISTA DE COMPRAS')

qtd_produtos = int(input('qtd. produtos:'))

lista_compras = []

while len(lista_compras) < qtd_produtos:
    nome_produto = input('Produto:')
    valor_produto = float(input('Valor:'))
    somatorio = 0
    item = {
        'nome': nome_produto,
        'valor': valor_produto
    }

    lista_compras.append(item)

print('Produtos:')

for item in lista_compras:
    print(item.get('nome'), 'R$', item.get('valor'))
    somatorio += item.get('valor')
            #"+=" serve para acrescentar um numero na variavel(para somar com os ja existentes)
print('Todos os Produtos custaram:', somatorio)