from listapersona import ListaPersona
import pytest

@pytest.fixture
def lista():
    return ListaPersona()

# Test de la clase ListaAlumnos
def test_listaPersona0(lista):
    assert len(lista) == 0

def test_listaPersona1(lista):
    lista.agregar("Alvaro")
    assert len(lista) == 1

def test_listaPersona2(lista):
    lista.agregar("Alvaro")
    lista.agregar("Zsofia")

    assert len(lista) == 2

    assert lista[0] == "Alvaro"
    assert lista[1] == "Zsofia"

def test_listaPersonaDelete(lista):
    lista.agregar("David")
    assert lista[0] == "David"

    del lista[0]
    assert len(lista) == 0

    assert "David" not in lista

def test_listaPersonaRead(lista):
    lista.agregar("Alvaro")
    lista.agregar("Zsofia")

    assert lista.read() == "Alvaro" + lista.LIMITCHAR + "Zsofia"

def test_listaPersonaLoad(lista):
    lista.load("Alvaro" + lista.LIMITCHAR + "David")
    assert len(lista) == 2

    assert lista[0] == "Alvaro"
    assert lista[1] == "David"