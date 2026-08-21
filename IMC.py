# Autor: Beatriz Conrado
# Projeto: Calculadora de IMC

print('======= Calculadora de IMC =======\n')
peso = float(input('digite o seu peso (kg):  '))
altura = float(input('digite a sua altura (m):  '))
imc = peso / (altura*altura)
print(f'Seu IMC é: {imc:.2f}')

#estrutura condicional
if imc <= 18.5: 
    print('Cuidado!! Magreza')
elif imc <= 25.0:
    print('Parabéns!!! Saudável')
elif imc <= 30.0:
    print('Alerta!! Você está com sobrepeso.')
elif imc <= 35.0:
    print('Cuidado!! Obesidade Grau I')
elif imc <= 40.0:
    print('Muito cuidado!! Obesidade Grau II')
else:
    print('Alerta Máximo!!! Obesidade Grau III')
    