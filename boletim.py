# Autor: Beatriz Conrado
# Projeto: Utilizando IF/ELIF/ELSE

# definição das variáveis
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1+nota2)/2
print(f'A média é:{media:.2f}') # Se a média for < que 7 então Aluno Reprovado

# Estrutura condicional 
# Se a média for >= 7 então Aluno Aprovado
if media >= 7:
   # \n serve para pular uma linha
   # :.2f serve para deixar um número em duas casas decimais
    print('aluno Aprovado!\n😂')
else:
    print('aluno reprovado!\n💔')