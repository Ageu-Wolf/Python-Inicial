from datetime import datetime,date
nome = input('nome:')
data_nascimento = input('Data de Nascimento:')

#converter string para date
data_nascimento = datetime.strptime(data_nascimento,'%d/%m/%Y').date()

#calcular idade
idade = (date.today() - data_nascimento).days / 365

if idade >= 18:
    print('Maior de idade')

else:
    print('Menor de idade') 