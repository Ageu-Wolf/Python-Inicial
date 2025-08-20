from datetime import datetime, date
maximo = 35
minimo = 30
lista_V = []
print('Classificação Vacinal:')

pessoas = int(input('Quantas pessoas irão se vacinar?'))
print('Idade mínima:', minimo)
print('Idade máxima:', maximo)

for vacinados in range(1, pessoas +1):
    print('Adicionar a pessoa', vacinados, ':')
    nome = input('Nome:')
    dt_nasc =  input('Data de nascimento:')

    dt_nasc =datetime.strptime(dt_nasc, '%d/%m/%Y').date()
    idade = (date.today() - dt_nasc).days / 365
    dt_nasc= dt_nasc.strftime('%d/%m/%Y')

    if idade >= 30 and idade <= 35:
        lista_V.append(nome)
        print(nome, 'foi adicionado na lista para vacinação!')
    else:
        print('Está fora do periodo de vacinação!')

for nome in lista_V:
    print(nome)