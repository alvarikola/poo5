import pytest 

from prueba28.jugador.persona import Persona

@pytest.fixture
def persona():
    return Persona("William")


def test_create(persona):
    assert persona.read() == "William"


def test_read(persona):
    assert persona.read() == "William"


def test_update(persona):
    persona.update("Alvaro")
    assert persona.read() == "Alvaro"


def test_delete(persona):
    persona.delete()
    assert persona.read() == None


