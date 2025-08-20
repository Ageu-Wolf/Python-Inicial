matriz1 = [
    [0,1,0],
    [1,1,1],
    [0,0,1],
]

print(matriz1[0][1])
#            '0' linha, '1'coluna

for linha in matriz1:
    for coluna in linha:
        print(coluna)


for i in range(0,3):
    for j in range(0,3):
        print(matriz1[i][j])