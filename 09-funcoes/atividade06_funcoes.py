# Autor: Beatriz Conrado
# Projeto: Funções conversão real X dolar (API + funções)

import requests

def converter_dolar_para_real(valor_dolares):
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    resposta = requests.get(url)
    dados = resposta.json()

    cotacao = float(dados["USDBRL"]["bid"])
    convertido = valor_dolares * cotacao

    return cotacao, convertido

##
valor = float(input("Digite o valor em dolares: ").strip())
cotacao_atual, valor_convertido = converter_dolar_para_real(valor)

print(f"Cotação: R$ {cotacao_atual:.4f}")
print(f"Valor original: US$ {valor:.4f}")
print(f"Valor convertido: R$ {valor_convertido:.4f}")
