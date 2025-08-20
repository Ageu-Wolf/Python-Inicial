chamada = ['Murilo', 'Manuela', 'Sara', 'Ageu']

print(chamada)

chamada_ordenada = sorted(chamada)
#sorted deixa em ordem alfabética ou de 0 a 100
print(chamada_ordenada)

chamada_ordenada_za = sorted(chamada, reverse=True)
#reverse=True,ordena de Z a A - reverse=false,ordenade A a Z 
print(chamada_ordenada_za)

print('Lista de todos os alunos:')
for aluno in chamada_ordenada:
    print('Aluno:',aluno)
