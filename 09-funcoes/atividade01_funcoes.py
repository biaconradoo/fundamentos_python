# Autor: Beatriz Conrado
# Projeto: trabalhando com funcoes

# estrutura sem funcao

base = float (input('valor da base: '))
altura = float (input('valor da altura: '))
area_triangulo = (base*altura)/2
print(f'A área do triangulo é: {area_triangulo:.2f}')

# estrutura com funcao
def calc_area_triangulo (b,a):
    area = (b*a)/2
    return area

base = float(input('valor da base: '))
altura = float(input('valor da altura: '))
resultado = calc_area_triangulo(base,altura)
print(f'A área do triangulo é: {area_triangulo:.2f}')