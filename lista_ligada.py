'''Testei os codigos no collab pois não consegui com o pytest, 
mas eu coloquei os arquivos no vs code e enviei..'''

'''depois de umas alterações, rodou no vs code também! editei este arquivo.'''

# %%writefile lista_ligada.py - collab

    def __init__(self):
        self.primeiro: No = None
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
        """Retorna os itens da lista em formato de string"""

        atual = self.primeiro
        resultado = ""

        while atual:
            resultado += str(atual.item) + " -> "
            atual = atual.proximo

        return resultado + "null"

    def pesquisar(self, item):
        """Retorna True se o item existir na lista"""

        atual = self.primeiro

        while atual:
            if atual.item == item:
                return True

            atual = atual.proximo

        return False

    def obter(self, posicao):
        """Retorna o item de uma determinada posição"""

        if posicao < 0 or posicao >= self.tamanho:
            return None

        atual = self.primeiro
        contador = 0

        while contador < posicao:
            atual = atual.proximo
            contador += 1

        return atual.item

    def inserir(self, posicao, item):
        """Insere um item em uma determinada posição"""

        if posicao < 0 or posicao > self.tamanho:
            return False

        novo_no = No(item)

        if posicao == 0:
            novo_no.proximo = self.primeiro
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            contador = 0

            while contador < posicao - 1:
                atual = atual.proximo
                contador += 1

            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

        self.tamanho += 1

        return True

    def remover(self, posicao):
        """Remove um item de uma determinada posição"""

        if posicao < 0 or posicao >= self.tamanho:
            return False

        if posicao == 0:
            self.primeiro = self.primeiro.proximo
        else:
            atual = self.primeiro
            contador = 0

            while contador < posicao - 1:
                atual = atual.proximo
                contador += 1

            atual.proximo = atual.proximo.proximo

        self.tamanho -= 1

        return True

    def remover_item(self, item):
        """Remove a primeira ocorrência de um item"""

        atual = self.primeiro
        anterior = None

        while atual:

            if atual.item == item:

                if anterior is None:
                    self.primeiro = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                self.tamanho -= 1

                return True

            anterior = atual
            atual = atual.proximo

        return False

    
