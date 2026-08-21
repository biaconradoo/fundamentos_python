# Autor: Beatriz Conrado
# Projeto: Motorista1 if/else | and | string | variáveis

idade = int(input('digite sua idade: '))
carteira = True
nome = input('Digite seu nome: ')

# Estrutura condicional
# and -> todas as condições tem que ser verdadeiras 
if idade >= 18 and carteira:
   print ('Pode dirigir')
else: 
   print ('Não pode dirigir')
