import pytest
from src.anagrams import group_anagrams

def normalize(groups):
    return sorted([sorted(g) for g in groups], key=lambda g: g[0] if g else "")

@pytest.mark.parametrize(
    "inp, expected",
    [
        (
            ["eat","tea","tan","ate","nat","bat"],
            [["bat"], ["nat","tan"], ["ate","eat","tea"]],
        ),
        (
            [],
            [],
        ),
        (
            ["a"],
            [["a"]],
        ),
        (
            ["", ""],
            [["",""]],
        ),
        (
            ["абв", "бав", "вба", "гд"],  # Юникод тоже работает
            [["гд"], ["абв","бав","вба"]],
        ),
        (
            ["no", "on", "no"],  # дубликаты должны быть сохранены
            [["no","no","on"]],
        ),
    ],
)
def test_group_anagrams(inp, expected):
    got = group_anagrams(inp)
    assert normalize(got) == normalize(expected)