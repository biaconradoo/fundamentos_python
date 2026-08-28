# Autor: Beatriz Conrado
# Projeto: Listas

# Lista de frutas com 5 unidades
#            0         1        2          3        4
frutas = ['banana', 'maçã', 'abacaxi', 'goiaba', 'kiwi']

print(frutas)

#Adição de um item na lista
frutas.append('laranja')
print(frutas)
#            0         1        2          3        4        5
#frutas= ['banana', 'maçã', 'abacaxi', 'goiaba', 'kiwi', 'laranja']

# Alterar o conteúdo de uma posição
# Mudar a fruta Kiwi para morango
frutas[4] = 'morango' 
print(frutas)
#            0         1        2          3          4
#frutas= ['banana', 'maçã', 'abacaxi', 'goiaba', 'morango']

# Deletar um item por posição
# excluir a maçã
del frutas [1]
print(frutas)
#            0         1        2          3        
#frutas= ['banana', 'abacaxi', 'goiaba', 'morango']

# Inserir uma nova fruta na lista
frutas.insert(1,'mamão')
print(frutas)
#            0         1        2          3           4
#frutas= ['banana', 'abacaxi', 'goiaba', 'morango', 'mamão']

# Deixar a lista em ordem alfabética
frutas.sort()
print(frutas)