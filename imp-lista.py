"""
Implemente uma função que recebe uma lista, o tamanho dela e um número inteiro e pesquisa se esse número existe na lista.
Se o número existe na lista, a função retorna True. Em caso contrário, retorna False.
Depois, crie uma lista com 5 números inteiros e teste sua função.

OBS: A resposta abaixo está incompleta. Finalize a função pesquisar. 
Instruções: Não use a palavra reservada in. Use um for para percorrer a lista e comparar cada número dela com o número pesquisado.
"""

def pesquisar(lista, tamanho, numero):
    

    for i in range(tamanho):
        if lista[i] == numero:
            return True

    return False

lista = [3, 5, 8, 10, 15]
tamanho = 5

print(f"Achou o 10 ? = {pesquisar(lista, tamanho, 10)}") # Deve imprimir True
print(f"Achou o 3  ? = {pesquisar(lista, tamanho, 3)}")  # Deve imprimir True
print(f"Achou o 6  ? = {pesquisar(lista, tamanho, 6)}")  # Deve imprimir False
print(f"Achou o 1  ? = {pesquisar(lista, tamanho, 1)}")  # Deve imprimir False+++