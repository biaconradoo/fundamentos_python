# Autor: Beatriz Conrado
# Projeto: 
# função calculadora

a = float(input('valor de a: '))
b = float(input('valor de b: '))
soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b
def calc_soma(a, b):
    soma=a+b
    return soma

def calc_subtracao(a,b):
    subtracao=a-b
    return subtracao

def calc_multiplicacao(a,b):
    multiplicacao=a*b
    return multiplicacao

def calc_divisao(a,b):
    divisao=a/b
    return divisao

print(f'O resultado da soma é: {soma}')
print(f'O resultado da subtracao é: {subtracao}')
print(f'O resultado da multiplicacao é: {multiplicacao}')
print(f'O resultado da divisao é: {divisao}')