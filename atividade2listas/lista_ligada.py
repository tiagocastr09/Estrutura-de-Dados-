from no import No


class ListaLigada:

    def __init__(self):
        self.primeiro: No = None
        self.tamanho = 0

    def inserir_inicio(self, item):
        """ Adiciona no início da lista
        Custo: O(1). pq ele troca duas referências e não percorre a lista """

        novo_no = No(item)
        novo_no.proximo = self.primeiro
        self.primeiro = novo_no
        self.tamanho += 1

    def __str__(self):
        """ Monta uma string com os itens da lista. 
        Custo: O(n) porque ele percorre todos os nós uma vez"""

        no_atual = self.primeiro
        string = ""

        while no_atual:
            string += str(no_atual.item) + " -> "
            no_atual = no_atual.proximo

        return string + "null"

    def adicionar(self, item):
        """ Adiciona no fim da lista
        Custo: O(n), ele percorre a lista até o último nó.
        (Melhor caso, lista vazia: O(1).) """

        novo_no = No(item)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1

    def pesquisar(self, item):
        """ Retorna True caso o item procurado exista na lista e
        False, em caso contrário.
        Custo: O(n) no pior caso (ultimo item), melhor caso: O(1) (item é o primeiro) """

        atual = self.primeiro
        while atual:
            if atual.item == item:
                return True
            atual = atual.proximo
        return False

    def obter(self, posicao):
        """ Retorna o item guardado em uma determinada posição da lista.
        Caso a posição não exista na lista, retorna None.
        Custo: O(n) no pior caso (última posição), melhor caso: O(1) (posição 0)"""

        if posicao < 0 or posicao >= self.tamanho:
            return None

        atual = self.primeiro
        for _ in range(posicao):
            atual = atual.proximo
        return atual.item

    def inserir(self, posicao, item):
        """ Adiciona um item em uma posição da lista
        empurrando os demais itens para o fim da lista.
        Se a posição não é válida, retorna False. 
         Custo: O(n) no pior caso (inserir no final), pois precisa chegar até o nó anterior.
         Melhor caso: O(1) (posição 0). """

        if posicao < 0 or posicao > self.tamanho:
            return False

        if posicao == 0:
            self.inserir_inicio(item)
            return True

        anterior = self.primeiro
        for _ in range(posicao - 1):
            anterior = anterior.proximo

        novo_no = No(item)
        novo_no.proximo = anterior.proximo
        anterior.proximo = novo_no
        self.tamanho += 1
        return True

    def remover_inicio(self):
        """ Remove o primeiro item da lista e o retorna 
        Custo: O(1). Só move a referência do primeiro nó.
        Se a lista estiver vazia, retorna None. """

        if self.primeiro is None:
            return None

        item = self.primeiro.item
        self.primeiro = self.primeiro.proximo
        self.tamanho -= 1
        return item

    def remover(self, posicao):
        """ Remove um item de uma posição da lista
        e puxa os demais itens para o início da lista.
        Ao final, retorna True. Caso a posição não exista na lista, retorna False. 
        Custo: O(n) no pior caso (remover o último), pois precisa chegar até o nó anterior.
        Melhor caso: O(1) (posição 0). """

        if posicao < 0 or posicao >= self.tamanho:
            return False

        if posicao == 0:
            self.remover_inicio()
            return True

        anterior = self.primeiro
        for _ in range(posicao - 1):
            anterior = anterior.proximo

        anterior.proximo = anterior.proximo.proximo
        self.tamanho -= 1
        return True

    def remover_item(self, item):
        """ Remove um item existente na lista e retorna True.
        Caso o item não seja encontrado, retorna False. 
        Custo: O(n) no pior caso (item no final), porque percorre a lista.
        Melhor caso: O(1) (item é o primeiro)."""

        anterior = None
        atual = self.primeiro
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
