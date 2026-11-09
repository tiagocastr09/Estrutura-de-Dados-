from lista_ligada import ListaLigada


def test_inserir_inicio():
    lista = ListaLigada()
    lista.adicionar(10)
    lista.inserir_inicio(5)
    assert str(lista) == "5 -> 10 -> null"


def test_str():
    lista = ListaLigada()
    lista.adicionar(10)
    lista.adicionar(20)
    assert str(lista) == "10 -> 20 -> null"


def test_adicionar():
    lista = ListaLigada()
    lista.adicionar(10)
    lista.adicionar(20)
    assert str(lista) == "10 -> 20 -> null"


def test_pesquisar():
    lista = ListaLigada()
    lista.adicionar(10)
    assert lista.pesquisar(10) is True
    assert lista.pesquisar(99) is False


def test_obter():
    lista = ListaLigada()
    lista.adicionar(10)
    lista.adicionar(20)
    assert lista.obter(1) == 20
    assert lista.obter(9) is None


def test_inserir():
    lista = ListaLigada()
    lista.adicionar(10)
    lista.adicionar(30)
    lista.inserir(1, 20)
    assert str(lista) == "10 -> 20 -> 30 -> null"


def test_remover_inicio():
    lista = ListaLigada()
    lista.adicionar(10)
    lista.adicionar(20)
    assert lista.remover_inicio() == 10
    assert str(lista) == "20 -> null"


def test_remover():
    lista = ListaLigada()
    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)
    lista.remover(1)
    assert str(lista) == "10 -> 30 -> null"


def test_remover_item():
    lista = ListaLigada()
    lista.adicionar(10)
    lista.adicionar(20)
    lista.remover_item(20)
    assert str(lista) == "10 -> null"