# Aprendizado Básico de Python

Bem-vindo(a) ao seu guia de aprendizado básico de Python! Este `README` foi criado para ajudar quem está começando a dar os primeiros passos na linguagem. Aqui, você encontrará os conceitos fundamentais, exemplos práticos e recursos úteis para sua jornada.

---

### 1. Configurando Seu Ambiente

Antes de começar a programar, você precisa ter o Python instalado.

* **Download:** Baixe a versão mais recente do Python no site oficial: [python.org](https://www.python.org/).
* **Editor de Código:** Recomenda-se usar um editor de código como o **VS Code**, que oferece diversas extensões para facilitar a escrita e a depuração do código. Você pode baixá-lo aqui: [code.visualstudio.com](https://code.visualstudio.com/).

---

### 2. Sintaxe Básica e Tipos de Dados

A sintaxe do Python é conhecida por ser clara e fácil de ler.

#### Variáveis

Variáveis são usadas para armazenar dados. Você não precisa declarar o tipo, o Python faz isso automaticamente.

```python
# Criando algumas variáveis
nome = "Maria"        # String (texto)
idade = 25            # Integer (número inteiro)
altura = 1.65         # Float (número decimal)
esta_estudando = True # Boolean (verdadeiro ou falso)

# Exibindo os valores
print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Estudando: {esta_estudando}")

Tipos de Dados
String (str): Sequência de caracteres. Ex: "Olá, mundo!"

Integer (int): Números inteiros. Ex: 10, -5

Float (float): Números decimais. Ex: 3.14, -0.5

Boolean (bool): Valores True ou False.

List (list): Coleção ordenada e mutável de itens.

Python

frutas = ["maçã", "banana", "uva"]
print(frutas[0]) # Acessa o primeiro item (maçã)
Tuple (tuple): Coleção ordenada e imutável de itens.

Python

coordenadas = (10, 20)
Dictionary (dict): Coleção não ordenada de pares de chave-valor.

Python

pessoa = {"nome": "João", "idade": 30}
print(pessoa["idade"]) # Acessa o valor da chave 'idade'
3. Estruturas de Controle de Fluxo
Essas estruturas permitem que você controle a ordem em que o seu código é executado.

Condicionais (if, elif, else)
Executa um bloco de código apenas se uma condição for verdadeira.

Python

idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
Laços de Repetição (for, while)
Repete um bloco de código várias vezes.

for: Usado para iterar sobre uma sequência (lista, tupla, string).

Python

for numero in range(5): # O laço vai de 0 a 4
    print(numero)
while: Continua executando enquanto a condição for verdadeira.

Python

contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1 # Incrementa o contador
4. Funções
Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas ajudam a organizar o código e evitam a repetição.

Python

# Definindo uma função
def saudacao(nome):
    return f"Olá, {nome}!"

# Chamando a função
mensagem = saudacao("Pedro")
print(mensagem) # Saída: Olá, Pedro!
5. Recursos Adicionais
Documentação Oficial do Python: docs.python.org - A melhor fonte de informações sobre a linguagem.

Codecademy: codecademy.com - Cursos interativos com exercícios práticos.

w3schools: w3schools.com/python/ - Tutoriais simples e diretos para iniciantes.

Dicas Finais
Pratique regularmente. A melhor forma de aprender é escrevendo código.

Não tenha medo de errar. Erros são parte do processo de aprendizado.

Leia códigos de outros desenvolvedores. Isso ajuda a entender diferentes abordagens e boas práticas.
