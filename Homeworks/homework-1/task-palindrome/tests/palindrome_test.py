import pytest
from src.palindrome import isPalindrome

@pytest.mark.parametrize("n,expected", [
    (121, True),        # простое палиндромное число
    (-121, True),       # отрицательное палиндромное число
    (12321, True),      # больше цифр
    (123, False),       # не палиндром
    (10, False),        # ведущий ноль в реверсе
    (0, True),          # ноль — палиндром
    (7, True),          # однозначное число всегда палиндром
])
def test_is_palindrome(n, expected):
    assert isPalindrome(n) == expected
