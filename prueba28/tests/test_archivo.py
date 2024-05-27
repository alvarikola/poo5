from listapersona import ListaPersona
from archivo import Archivo
import pytest
import os

FILENAME = 'lista.dat'
DATA    = 'Alvaro' + ListaPersona.LIMITCHAR + 'Zsofia'

@pytest.fixture
def archivo():
    return Archivo(FILENAME)

def test_archivoLeer(archivo):
    os.remove(FILENAME)
    assert archivo.leer() == ""

def test_archivoEscribir(archivo):
    assert archivo.escribir(DATA) == True

def test_archivoLeer2(archivo):
    assert archivo.leer() == DATA

def test_archivoListaTareas(archivo):
    lista = ListaPersona()
    lista.load(archivo.leer())
    assert lista.read() == DATA