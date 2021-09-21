import pytest

from insofee.myapp.mymodule.funcs import add


@pytest.mark.parametrize("a,b,c", [(10, 20, 30), (11, 20, 31), (12, 13, 25)])
def test_add(a, b, c):
    result = add(a, b)
    assert result == c
