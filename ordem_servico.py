from datetime import datetime, timedelta, date


nome = input('Nome do cliente:')
telefone = input('Telefone:')
descricao_p = input('Descrição do produto:')
descricao_d= input('Decrição do defeito:')


hoje = datetime.today()
prazo = hoje + timedelta(days=7)
prazo1 = prazo.strftime('%d/%m/%Y')


print(nome)
print(telefone)
print(descricao_p)
print(descricao_d)

print(30*'-')
print('Prazo calculado para entrega do orçamento:')
print(prazo1)
