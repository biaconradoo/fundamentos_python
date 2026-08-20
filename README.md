# fundamentos_python
🐍 Fundamentos de Python

Este repositório apresenta os conceitos fundamentais para quem está começando a programar em Python, com exemplos práticos e simples.

Neste material, você aprenderá:

📦 Variáveis
🖨️ print()
🧩 f-string
🔀 if
🔄 elif
🧱 else
📚 Índice
Variáveis
Função print()
f-string
Estrutura if
Estrutura elif
Estrutura else
Exemplo completo
Conclusão
📦 Variáveis

Uma variável é um espaço utilizado para armazenar informações que podem ser utilizadas posteriormente pelo programa.

Em Python, não é necessário declarar previamente o tipo da variável.

Exemplo
nome = "Maria"
idade = 25
altura = 1.68
estudante = True


Nesse exemplo:

nome armazena um texto (str)
idade armazena um número inteiro (int)
altura armazena um número decimal (float)
estudante armazena um valor lógico (bool)

Podemos verificar o tipo de uma variável utilizando type():

nome = "Maria"

print(type(nome))


Saída:

<class 'str'>

💡 Boas práticas

Prefira nomes de variáveis que expliquem o que elas representam:

idade_usuario = 25
nome_cliente = "João"
valor_produto = 99.90


Evite nomes pouco descritivos:

x = 25
a = "João"
v = 99.90

🖨️ Função print()

A função print() é utilizada para exibir informações no terminal.

Exemplo simples
print("Olá, mundo!")


Saída:

Olá, mundo!


Também podemos imprimir variáveis:

nome = "Maria"

print(nome)


Saída:

Maria


Podemos imprimir diferentes valores:

nome = "Maria"
idade = 25

print(nome)
print(idade)

🧩 f-string

As f-strings facilitam a criação de textos que precisam utilizar valores armazenados em variáveis.

Para utilizar uma f-string, colocamos a letra f antes das aspas e usamos {} para inserir as variáveis.

Exemplo
nome = "Maria"
idade = 25

print(f"Meu nome é {nome} e tenho {idade} anos.")


Saída:

Meu nome é Maria e tenho 25 anos.

Por que utilizar f-string?

Sem f-string, poderíamos fazer:

nome = "Maria"
idade = 25

print("Meu nome é", nome, "e tenho", idade, "anos.")


Com f-string:

print(f"Meu nome é {nome} e tenho {idade} anos.")


A segunda opção costuma ser mais legível e prática.

🔀 Estrutura if

O if é utilizado para executar um determinado bloco de código quando uma condição for verdadeira.

Sintaxe
if condição:
    # código executado se a condição for verdadeira

Exemplo
idade = 18

if idade >= 18:
    print("Você é maior de idade.")


Como 18 >= 18 é verdadeiro, o programa executará o print().

⚠️ Indentação

A indentação é fundamental em Python.

Correto:

if idade >= 18:
    print("Maior de idade")


Incorreto:

if idade >= 18:
print("Maior de idade")


A indentação indica quais instruções pertencem ao bloco do if.

🔄 Estrutura elif

O elif significa "else if" e permite verificar uma nova condição caso a condição anterior não seja verdadeira.

Exemplo
idade = 15

if idade >= 18:
    print("Maior de idade")
elif idade >= 13:
    print("Adolescente")


Nesse caso:

O Python verifica idade >= 18.
Como é falso, verifica idade >= 13.
Como é verdadeiro, executa o segundo bloco.

Podemos utilizar vários elif:

nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")

🧱 Estrutura else

O else representa uma alternativa que será executada quando nenhuma das condições anteriores for verdadeira.

Exemplo
idade = 15

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


Como 15 >= 18 é falso, o programa executará:

Menor de idade

🔀 Combinando if, elif e else

Podemos utilizar as três estruturas juntas para criar decisões mais completas.

nota = 8

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")


Resultado:

Aprovado

Fluxo da decisão
             ┌───────────────┐
             │   nota >= 9?  │
             └───────┬───────┘
                     │
             Sim ────┴───> Excelente
                     │
                    Não
                     ↓
             ┌───────────────┐
             │   nota >= 7?  │
             └───────┬───────┘
                     │
             Sim ────┴───> Aprovado
                     │
                    Não
                     ↓
                  Reprovado

🚀 Exemplo completo

A seguir, temos um pequeno programa utilizando variáveis, print(), f-string, if, elif e else:

nome = "Carlos"
idade = 20
nota = 8.5

print(f"Aluno: {nome}")
print(f"Idade: {idade}")
print(f"Nota: {nota}")

if nota >= 9:
    resultado = "Excelente"
elif nota >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print(f"Resultado: {resultado}")


Saída:

Aluno: Carlos
Idade: 20
Nota: 8.5
Resultado: Aprovado

🧠 Resumo
Conceito	Função
Variável	Armazena informações
print()	Exibe informações
f-string	Facilita a inserção de variáveis em textos
if	Executa código quando uma condição é verdadeira
elif	Verifica uma nova condição
else	Executa quando nenhuma condição anterior é verdadeira
🎯 Conclusão

Esses conceitos são uma excelente base para começar a desenvolver aplicações em Python.

A combinação de variáveis + saída de dados + f-strings + estruturas condicionais permite criar programas capazes de armazenar informações, apresentar resultados e tomar decisões.

A partir desses fundamentos, é possível avançar para conceitos como:

🔁 Laços for e while
📋 Listas e dicionários
🔧 Funções
📦 Módulos e pacotes
🛡️ Tratamento de exceções
🏗️ Programação orientada a objetos

Pratique: a melhor forma de aprender programação é escrever código, testar, cometer erros e entender como corrigi-los. 🚀
