# Autor: Beatriz Conrado
# Projeto: Juros Simples

# Fórmula :  J = C × i × t

c = float (input('Digite o valor inicial: '))
i= float (input('Digite o valor da taxa (decimal):'))
t = int (input('Digite o tempo: '))

j = c * i * t
valor = c + j
print(f' a taxa de juros é {j} e o valor é: {valor} ')