import pytest

from tarea import Tarea

@pytest.fixture
def tarea():
    return Tarea("Tarea1", False, 1)


def test_read(tarea):
    assert tarea.read() == "Tarea1, False, 1"


def test_update(tarea):
    tarea.update("Tarea1Nueva", True, 1)
    assert tarea.read() == "Tarea1Nueva, True, 1"


def test_delete(tarea):
    tarea.delete()
    assert tarea.read() == None

