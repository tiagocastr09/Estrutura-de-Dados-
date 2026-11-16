from no import No

class ListaLigada:

    def __init__(self):
        self.primeiro: No = None
        self.tamanho = 0


    def inserir_inicio(self, item):
        """ Adiciona no início da lista """
        
        novo_no = No(item)
        novo_no.proximo = self.primeiro
        self.primeiro = novo_no
        self.tamanho += 1


    def __str__(self):
        """ Monta uma string com os itens da lista """

        no_atual = self.primeiro
        string = ""

        while no_atual:
            string += str(no_atual.item) + " -> "
            no_atual = no_atual.proximo

        return string + "null"


    def adicionar(self, item):
        """ Adiciona no fim da lista """

        novo_no = No(item)
        if self.vazia():
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1


    def pesquisar(self, item):
        """ Retorna True caso o item procurado exista na lista e
        False, em caso contrário. """

        atual = self.primeiro
        while atual:
            if atual.item == item:
                return True
            atual = atual.proximo
        return False


    def obter(self, posicao):
        """ Retorna o item guardado em uma determinada posição da lista.
        Caso a posição não exista na lista, retorna None. """
        
        if 0 <= posicao < self.tamanho:
            atual = self.primeiro
            for i in range(posicao): 
                atual = atual.proximo
            return atual.item
        
        return None


    def inserir(self, posicao, item):
         """ Adiciona um item em uma posição da lista
        empurrando os demais itens para o fim da lista.
        Se a posição não é válida, retorna False. """
         
         if 0 <= posicao <= self.tamanho:
            if posicao == 0:
                self.inserir_inicio(item)
            else:
                novo_no = No(item)
                atual = self.primeiro
                for i in range(posicao - 1):
                    atual = atual.proximo
                novo_no.proximo = atual.proximo
                atual.proximo = novo_no
            self.tamanho += 1
            return True
         return False

    def remover_inicio(self):
        """ Remove o primeiro item da lista e o retorna """

        if self.vazia():
            return None
        
        item_removido = self.primeiro.item
        self.primeiro = self.primeiro.proximo
        self.tamanho -= 1

        return item_removido        


    def remover(self, posicao):
        """ Remove um item de uma posição da lista
        e puxa os demais itens para o início da lista.
        Ao final, retorna o item removido. Caso a posição não exista na lista ou se a lista estiver vazia, retorna None. """

        if not self.vazia() and 0 <= posicao < self.tamanho:
            if posicao == 0:
                return self.remover_inicio()
            else:
                atual = self.primeiro
                for i in range(posicao - 1):
                    atual = atual.proximo
                item_removido = atual.proximo.item
                atual.proximo = atual.proximo.proximo
                self.tamanho -= 1
                return item_removido
        return None


    def remover_item(self, item):
        """ Remove um item existente na lista e retorna True.
        Caso o item não seja encontrado, retorna False. """

        if self.vazia():
            return False
        
        if self.primeiro.item == item:
            self.remover_inicio()
            return True
        
        atual = self.primeiro
        while atual.proximo:
            if atual.proximo.item == item:
                atual.proximo = atual.proximo.proximo
                self.tamanho -= 1
                return True
            atual = atual.proximo
        
        return False

    def vazia(self):
        return self.tamanho == 0
