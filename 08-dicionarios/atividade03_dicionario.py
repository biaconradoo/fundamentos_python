# Autor: Beatriz Conrado
# Projeto:

import requests

# Uso da API de cotações
url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
resposta = requests.get(url)
dados = resposta.json()

# Variáveis das moedas
valor_dolar = dados ['USDBRL']['bid']
valor_euro = dados ['EURBRL']['bid']
valor_btc = dados ['BTCBRL']['bid']

print(f"Cotação do dolar: {valor_dolar}")
print(f"Cotação do euro: {valor_euro}")
print(f"Cotação Bitcoin: {valor_btc}")