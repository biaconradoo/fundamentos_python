# Autor: Beatriz Conrado
# Projeto: Funções 

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
soma = valor1+valor2
subtracao = valor1-valor2
multiplicacao = valor1*valor2
divisao = valor1/valor2
print(f'O valor da soma é: {soma}')
print(f'O valor da subtracao é: {subtracao}')
print(f'O valor da multiplicacao é: {multiplicacao}')
print(f'O valor da divisao é: {divisao}')


# função calculadora
a = float(input('valor de a: '))
b = float(input('valor de b: '))

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
resultado = calc_soma(a,b)
resultado = calc_subtracao(a,b)
resultado = calc_multiplicacao(a,b)
resultado = calc_divisao(a,b)