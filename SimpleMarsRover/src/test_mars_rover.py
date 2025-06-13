import pytest
from src.mars_rover import MarsRover

@pytest.fixture
def rover():
    return MarsRover()
def test_posicao_inicial(rover):
    assert rover.execute("") == "0:0:N"

def test_movimento_frente(rover):
    assert rover.execute("M") == "0:1:N"

def test_girar_direita(rover):
    assert rover.execute("R") == "0:0:E"

def test_girar_esquerda(rover):
    assert rover.execute("L") == "0:0:W"

