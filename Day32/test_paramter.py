import pytest

def inputs():
    return [
        (1, 2, 3),
        (-1, -1, -2),
        (0, 0, 0),
        (0,2,-10)
    ]

@pytest.mark.parametrize("x, y, expected", inputs())
@pytest.mark.functional
@pytest.mark.regression
def test_add(x, y, expected):
    assert x + y == expected

