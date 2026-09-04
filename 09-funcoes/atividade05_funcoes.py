# Autor: Beatriz Conrado
# Projeto: Funções conversão real X dolar (API)

import requests

valor = float(input("Digite o valor em dolares: ").strip())

url = "https://economia.awesomeapi.com.br/last/USD-BRL"
resposta = requests.get(url)
dados = resposta.json()

cotacao = float(dados["USDBRL"]["bid"])
convertido = valor * cotacao

print (f"cotacao: R$ {cotacao:.4f}")
print (f"valor normal: US$ {valor:.4f}")
print (f"valor convertido: R$ {convertido:.4f}")
