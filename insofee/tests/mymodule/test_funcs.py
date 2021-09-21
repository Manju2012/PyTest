import pytest

from insofee.myapp.mymodule.funcs import add, sub, multiply, divide


@pytest.mark.easy_op
def test_add(a, b, c):
    assert add(a, b) == c


@pytest.mark.easy_op
def test_sub():
    assert sub(3, 6) == -3


@pytest.mark.easy_op
def test_mul():
    assert multiply(3, 4) == 12


@pytest.mark.easy_op
def test_div():
    assert divide(10, 2) == 5
