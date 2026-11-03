#fiquei em dúvida se devia completar os demais ou não, mas completei...
from no import No


class Lista_Ligada:

    def __init__(self):
        self.primeiro: No = None
        self.tamanho = 0

    def adicionar(self, item):
        """ Adiciona no fim da lista """

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
        """ Retorna uma string com os itens da lista. Ex.: '10 -> 20 -> null' """

        texto = ""
        no_atual = self.primeiro
        while no_atual:
            texto += f"{no_atual.item} -> "
            no_atual = no_atual.proximo
        texto += "null"
        return texto

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

        if posicao < 0 or posicao >= self.tamanho:
            return None

        atual = self.primeiro
        for _ in range(posicao):
            atual = atual.proximo
        return atual.item

    def inserir(self, posicao, item):
        """ Adiciona um item em uma posição da lista
        empurrando os demais itens para o fim da lista.
        Se a posição não é válida, retorna False. """

        if posicao < 0 or posicao > self.tamanho:
            return False

        novo_no = No(item)
        if posicao == 0:
            novo_no.proximo = self.primeiro
            self.primeiro = novo_no
        else:
            anterior = self.primeiro
            for _ in range(posicao - 1):
                anterior = anterior.proximo
            novo_no.proximo = anterior.proximo
            anterior.proximo = novo_no

        self.tamanho += 1
        return True

    def remover(self, posicao):
        """ Remove um item de uma posição da lista
        e puxa os demais itens para o início da lista.
        Ao final, retorna True. Caso a posição não exista na lista, retorna False. """

        if posicao < 0 or posicao >= self.tamanho:
            return False

        if posicao == 0:
            self.primeiro = self.primeiro.proximo
        else:
            anterior = self.primeiro
            for _ in range(posicao - 1):
                anterior = anterior.proximo
            anterior.proximo = anterior.proximo.proximo

        self.tamanho -= 1
        return True

    def remover_item(self, item):
        """ Remove um item existente na lista e retorna True.
        Caso o item não seja encontrado, retorna False. """

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
