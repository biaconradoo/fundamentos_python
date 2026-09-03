# Autor: Beatriz Conrado
# Projeto: Dicionarios

# Projeto aquele la
escola = {
    "salas": "sala_musica",
    "localizacao": "bloco_A",
    "qtd_lugares": "40",
    "caracteristica": "acustica"
}

# Acessando dados do dicionario:
print(f'Sala disponivel {escola["salas"]}')

# Adicionando mais itens ao dicionario
escola["iluminacao"] = "led"
print(f'Sala disponivel {escola["iluminacao"]}')

# Alterando um valor do dicionario
escola["salas"]  = "sala"
print(f'Sala disponivel {escola["salas"]}')
