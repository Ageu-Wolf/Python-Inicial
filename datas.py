from datetime import date, datetime, timedelta
from time import strptime

data1 = date(2006, 2, 18)

print(data1)
print(data1.year)
print(data1.month)
print(data1.day)

ano = data1.year
mes = data1.month
dia = data1.day

print(f'{dia}/{mes}/{ano}')

hoje = date.today()
print(hoje)

idade = (hoje - data1).days / 365

print(round(idade,2))

data2 = date(2023, 10, 7)
print(data2)

data2 = data2.replace(year=2022)
#Podemos alterar o ano,mes e dia ao mesmo tempo, separando cada um por virgula
print(data2)
#inicio "Datetime"
data_hora = datetime.today(),
print(data_hora)

agora = datetime.now()
print(agora)


agora = agora.replace(year=2022, 
                        month=12, day=31,  
                            hour=10, minute=20)
print(agora)
                                    #%Y-mostra os 4 digitos do ano, %y-mostra os dois ultimos digitos do ano
data_hora_string_br = agora.strftime('%d/%m/%Y %H:%M:%S')
    #"strftime" transforma em um texto, %d-dia,%m-mounth, %H-hour, %M-minute, %S-second
print(data_hora_string_br)

#date para string
dt_nasc = date(2006, 2, 18)
print(dt_nasc)

nasc = dt_nasc.strftime('%d/%m/%Y')
print(nasc)

data_string = '18/02/2006'

data_date = datetime.strptime(data_string, '%d/%m/%Y')

print(data_date)

data_a = date(2022, 2, 20)
data_b = date(2022, 3, 14)

print(data_a == data_b)
print(data_a > data_b)
print(data_a < data_b)

hoje = date.today()
dt_futura = hoje+ timedelta(days=30)

print(hoje, dt_futura)