# Autor: Beatriz Conrado
# Projeto: Desafio fatorial

# A expressão completa fica assim:
# 6! = 6 x 5 x 4 x 3 x 2 x 1 = 720

numero = int(input('Digite a fatorial desejada: '))
fatorial = 1

for i in range(1,numero+1):
    # cálculo da fatorial
    fatorial=fatorial*i

    # print do resultado
    print(f' Fatorial: {fatorial}')