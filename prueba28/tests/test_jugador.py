import pytest

from prueba28.jugador.jugador import Jugador

@pytest.fixture
def jugador():
    return Jugador("William", "Cricket")


def test_read(jugador):
    jugador.read() == "William,Cricket"


def test_update(jugador):
    jugador.update("Alvaro", "Voley")
    assert jugador.read() == "Alvaro,Voley"


def test_delete(jugador):
    jugador.delete()
    assert jugador.nombre == None
    assert jugador.deporte == None
