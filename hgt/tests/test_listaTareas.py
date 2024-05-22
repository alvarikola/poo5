from hgt.listaTareas import ListaTareas
import pytest

@pytest.fixture
def lista():
    return ListaTareas()

# Test de la clase ListaAlumnos
def test_listaTareas0(lista):
    assert len(lista) == 0

def test_listaTareas1(lista):
    lista.agregar("Tarea1")
    assert len(lista) == 1

def test_listaTarea2(lista):
    lista.agregar("Tarea1")
    lista.agregar("Tarea2")

    assert len(lista) == 2

    assert lista[0] == "Tarea1"
    assert lista[1] == "Tarea2"

def test_listaTareaDelete(lista):
    lista.agregar("Tarea3")
    assert lista[0] == "Tarea3"

    del lista[0]
    assert len(lista) == 0

    assert "Tarea3" not in lista

def test_listaRead(lista):
    lista.agregar("Tarea1 True 1")
    lista.agregar("Tarea2 False 2")

    assert lista.read() == "Tarea1 True 1" + lista.LIMITCHAR + "Tarea2 False 2"

def test_listaLoad(lista):
    lista.load("Tarea1 True 1" + lista.LIMITCHAR + "Tarea2 False 2")
    assert len(lista) == 2

    assert lista[0] == "Tarea1 True 1"
    assert lista[1] == "Tarea2 False 2"