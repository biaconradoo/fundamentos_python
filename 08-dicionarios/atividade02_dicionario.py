# Autor: Beatriz Conrado
# Projeto: Uso de API (conceito de dicionario)

# requisições http - GET
import requests

# Uso da API do ViaCEP
# 18.125-170 | 18125170 -> correto (apenas numeros, entao use strip().replace("-", ""))
cep = input("Digite seu CEP: ").strip().replace("-", "")

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
dados = resposta.json()

print(f"Logradouro: {dados['logradouro']}")
print(f"Bairro:  {dados['bairro']}")
print(f"Cidade:  {dados['localidade']}")