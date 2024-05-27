from listajugador import ListaJugador
import pytest

@pytest.fixture
def lista():
    return ListaJugador()

# Test de la clase ListaAlumnos
def test_listaJugador0(lista):
    assert len(lista) == 0

def test_listaJugador1(lista):
    lista.agregar("Alvaro")
    assert len(lista) == 1

def test_listaJugador2(lista):
    lista.agregar("Alvaro")
    lista.agregar("Zsofia")

    assert len(lista) == 2

    assert lista[0] == "Alvaro"
    assert lista[1] == "Zsofia"

def test_listaJugadorDelete(lista):
    lista.agregar("David")
    assert lista[0] == "David"

    del lista[0]
    assert len(lista) == 0

    assert "David,Nada" not in lista

def test_listaJugadorRead(lista):
    lista.agregar("Alvaro,Voley")
    lista.agregar("Zsofia,Baile")

    assert lista.read() == "Alvaro,Voley" + lista.LIMITCHAR + "Zsofia,Baile"

def test_listaJugadorLoad(lista):
    lista.load("Alvaro,Voley" + lista.LIMITCHAR + "David,Nada")
    assert len(lista) == 2

    assert lista[0] == "Alvaro,Voley"
    assert lista[1] == "David,Nada"