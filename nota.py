
print('Aplicativo Boletim')
print(20*'-')

nome = input('Nome do aluno:')
nota1 = float(input('Nota1:'))
nota2 = float(input('Nota2:'))
nota3 = float(input('Nota3:'))
nota_final = (nota1 + nota2 + nota3) / 3

print(nome.upper())
print('Nota Final:', round(nota_final, 2))


if nota_final >= 7:
    print('Aprovado')
else:
    print('Reprovado')