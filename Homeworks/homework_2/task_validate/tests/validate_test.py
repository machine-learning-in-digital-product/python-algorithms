import pytest
from src.validate import validate

@pytest.mark.parametrize("pushed,popped,expected", [
    # из условия
    ([1,2,3,4,5], [1,3,5,4,2], True),
    ([1,2,3], [3,1,2], False),

    # тривиальные
    ([1], [1], True),
    ([1,2], [2,1], True),
    ([1,2], [1,2], True),

    # разные порядки
    ([1,2,3,4], [2,1,4,3], True),
    ([1,2,3,4], [2,3,1,4], True),

    # длинные монотонные шаблоны
    (list(range(1,6)), list(range(5,0,-1)), True),
    (list(range(1,6)), [1,2,3,4,5], True),

    # рандомные/угловые
    ([1,2,3,4,5], [4,5,3,2,1], True),
    ([1,2,3,4,5], [4,3,5,1,2], False),
])
def test_validate_stack_sequences_param(pushed, popped, expected):
    assert validate(pushed, popped) == expected


def test_large_n_linear_time():
    n = 100_000
    pushed = list(range(n))
    popped = pushed[::-1]
    assert validate(pushed, popped) is True
