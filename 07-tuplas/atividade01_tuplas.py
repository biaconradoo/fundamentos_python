# Autor: Beatriz Conrado
# Projeto: Tuplas

meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov','dez')
print(meses)
#remover aspas e virgulas:
print(*meses)
#separador (pode ser | ou até mesmo ,)
print(*meses, sep=' | ')
