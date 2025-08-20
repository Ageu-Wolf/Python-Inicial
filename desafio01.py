print(50*'-')
print('Cálculo De Despesa Da Viagem:')


qtd_pessoas = int(input('Quantas Pessoas Irão viajar ?'))
custo_hospedagem_pessoa = float((input('Qual o Valor da Hospedagem ?')))

custo_total_hospedagem = qtd_pessoas * custo_hospedagem_pessoa

print('Despeza total de hospedagem é: R$', custo_total_hospedagem)


qntd_pedagios = int(input('Passaram por quantos pedágios ?'))
custo_unidade_pedagio = float(input('Quanto foi gasto em cada pedagio?'))

despeza_total_pedagios = custo_unidade_pedagio * qntd_pedagios

print('Foi gasto: R$',round(despeza_total_pedagios,3),'em todos os pedagios')

carro_Kml = float(input('quantos Km/L ?'))
distancia_total = float(input('Quantos Km foram percorridos ?'))
custo_litro_combustivel = float(input('Quanto custa cada litro de combustível?'))

despeza_total_combustivel = (distancia_total / carro_Kml) * custo_litro_combustivel 

print('Despeza Total de combustivel: R$',round(despeza_total_combustivel,2))

despesa_toda_viagem = despeza_total_combustivel + despeza_total_pedagios + custo_total_hospedagem

print('Despeza total geral da viagem: R$',round(despesa_toda_viagem,2))
print('Despesa total da hospedagem: R$',round(custo_total_hospedagem,2))
print('Despeza total pedágios: R$', round(despeza_total_pedagios,2))
print('Despesa total combustível: R$', round(despeza_total_combustivel,2))

print(20*'-')
print('Despesa total geral da viagem: R$',round(despesa_toda_viagem,2))




