import pytest

from insofee.myapp.app import multiply_by_two, divide_by_two


@pytest.fixture
def numbers():
    a = 10
    b = 20
    return a, b


class TestApp:
    def test_multiply(self, numbers):
        result = multiply_by_two(numbers[0])
        assert result == numbers[1]

    def test_div(self, numbers):
        result = divide_by_two(numbers[1])
        assert result == numbers[0]
