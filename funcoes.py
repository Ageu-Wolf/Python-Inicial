#"def" - definição da função" , "mensagem_game_over" - "nome da função, Assinatura da função(Parametros)"
def mensagem_game_over():
    print(30*'*')
    print('GAME OVER')
    print('Tente Novamente')
    print(30*'*')
print('Antes da função')
mensagem_game_over()
print('Depois da primeira')
mensagem_game_over()
print('Depois da segunda') 
print(50*'*')
print(50*'*')



def ola(nome, idade):
    print(f'Olá {nome}')
    print(f'Que legal, você tem {idade} anos!')
    print('Seja Bem-Vindo!')
idade_usuario = 16
nome_usuario = 'Ageu'
ola(nome=nome_usuario, idade=idade_usuario)



def somar(num1, num2):
    return num1 + num2
resultado = somar(num1=10, num2=35)

print(resultado)

def subtrair(num1, num2):
    return num1 - num2

resultado = subtrair(500, 300)
print(resultado)