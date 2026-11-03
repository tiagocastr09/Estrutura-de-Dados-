from lista_ligada import Lista_Ligada


def criar_lista():
    lista = Lista_Ligada()
    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)
    return lista


def test_adicionar():
    lista = criar_lista()
    lista.adicionar(40)
    assert lista.exibir() == "10 -> 20 -> 30 -> 40 -> null"


def test_exibir():
    lista = criar_lista()
    assert lista.exibir() == "10 -> 20 -> 30 -> null"


def test_pesquisar():
    lista = criar_lista()
    assert lista.pesquisar(20)


def test_obter():
    lista = criar_lista()
    assert lista.obter(1) == 20


def test_inserir():
    lista = criar_lista()
    lista.inserir(1, 15)
    assert lista.exibir() == "10 -> 15 -> 20 -> 30 -> null"


def test_remover():
    lista = criar_lista()
    lista.remover(1)
    assert lista.exibir() == "10 -> 30 -> null"


def test_remover_item():
    lista = criar_lista()
    lista.remover_item(20)
    assert lista.exibir() == "10 -> 30 -> null"
