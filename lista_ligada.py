'''Testei os codigos no collab pois não consegui com o pytest, 
mas eu coloquei os arquivos no vs code e enviei..'''

# %%writefile lista_ligada.py

from no import No

class Lista_Ligada:

    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    def adicionar(self, item):
        """Adiciona no fim da lista"""

        novo_no = No(item)

        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro

            while atual.proximo:
                atual = atual.proximo

            atual.proximo = novo_no

        self.tamanho += 1

    def exibir(self):
            atual = self.primeiro
            resultado = ""
        
            while atual:
                resultado += str(atual.item) + " -> "
                atual = atual.proximo
        
            return resultado + "null"

    def pesquisar(self, item):
        pass

    def obter(self, posicao):
        pass

    def inserir(self, posicao, item):
        pass

    def remover(self, posicao):
        pass

    def remover_item(self, item):
        pass

    