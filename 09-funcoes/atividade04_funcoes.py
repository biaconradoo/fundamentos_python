# Autor: Beatriz Conrado
# Projeto: Funções dentro de funções

#juros simples j= C + i * t
# montante M = C + J
def calcular ():
    def juros_simples(c,i,t):
        return c * i * t

# Juros compostos J = M - C
# montante M = C *(i+1)^t
    def juros_compostos(c,i,t):
        return c*(1+i)**t - c

    # Alternativas
    op = input('Escolha 1-Juros Simples ou 2-Juros compostos')

    #entrada de dados
    c = float(input('Digite o capital: '))
    i = float(input('Digite a taxa(Decimal): '))
    t = float(input('Digite as parcelas: '))

    # Condicionais que escolhem a operação
    if op == 1:
        print (juros_simples(c,i,t))
    else:
        print (juros_compostos(c,i,t))
   

calcular()