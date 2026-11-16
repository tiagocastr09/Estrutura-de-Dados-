
from pilha import Pilha


def decimal_para_binario(numero):
    pilha = Pilha()

    # Caso especial: zero em binário é 0
    if numero == 0:
        return "0"

    # Fase 1: empilhar os restos das divisões
    while numero > 0:
        resto = numero % 2
        pilha.empilhar(resto)
        numero = numero // 2

    # Fase 2: desempilhar os restos na ordem correta
    binario = ""

    while not pilha.vazia():
        binario += str(pilha.desempilhar())

    return binario


# Teste do algoritmo
numero = 13

resultado = decimal_para_binario(numero)

print(f"Decimal: {numero}")
print(f"Binário: {resultado}")
