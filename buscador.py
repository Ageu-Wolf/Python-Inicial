palavras = []

qtd_palavras = int(input('Quantas palavras ?'))

for i in range(1, qtd_palavras + 1):
    palavra_digitada = input('Informe a palavra:%d: ' % i)
    palavras.append(palavra_digitada)

busca = input('Qual palavra deseja buscar? ')

qtd_encontradas = palavras.count(busca)

if qtd_encontradas:
    #se existe pelo menos uma palavra encontrada
    if qtd_encontradas == 1:
        print('A palavra', busca, 'foi encontrada 1 vez.')
    else:
        print('A palavra', busca, 'foi encontrada', qtd_encontradas, 'vezes.')
else:
    #Se não existe nenhuma palavra encontrada
    print('A palavra', busca, 'não foi encontrada!')



