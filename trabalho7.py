# Função para calcular soma e média de uma lista de números
def calcular_soma_e_media(lista):
    # Verifica se a lista está vazia
    if len(lista) == 0:
        return "A lista está vazia."
    
    # Calcula a soma dos elementos na lista
    soma = sum(lista)
    
    # Calcula a média dos elementos na lista
    media = soma / len(lista)
    
    return soma, media

# Função para substituir ocorrências de uma palavra por outra em uma lista de palavras
def substituir_palavra(lista, palavra_procurada, nova_palavra):
    # Itera sobre cada palavra na lista
    for i in range(len(lista)):
        # Se a palavra na posição atual for igual à palavra procurada, substitua
        if lista[i] == palavra_procurada:
            lista[i] = nova_palavra
    return lista

# Função para gerar triângulo de asteriscos
def imprimir_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)

# Exemplo de uso das funções:

# 1. Calcular soma e média de uma lista de números
numeros = [1, 2, 3, 4]
soma, media = calcular_soma_e_media(numeros)
print("Soma:", soma)
print("Média:", media)

# 2. Substituir ocorrências de uma palavra por outra em uma lista de palavras
lista_palavras = ["roxo", "azul", "vermelho", "azul", "roxo"]
palavra_procurada = "roxo"
nova_palavra = "laranja"
lista_alterada = substituir_palavra(lista_palavras, palavra_procurada, nova_palavra)
print("Lista alterada:", lista_alterada)

# 3. Gerar triângulo de asteriscos para um número de linhas informado
n = 10
print("Triângulo de asteriscos para n =", n)
imprimir_triangulo(n)
