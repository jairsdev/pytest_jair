import pytest

@pytest.mark.parametrize("x, r", [
    (2, 4),
    (3, 5),
    (5, 7),
])

def soma(x):
    return x + 1

def test_soma(x, r):
    assert soma(x) == r


