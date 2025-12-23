import pytest

from src.kmp import kmp_search


def test_basic_match():
    assert kmp_search("ababcabcabababd", "ababd") == [10]


def test_multiple_matches():
    assert kmp_search("aaaaa", "aa") == [0, 1, 2, 3]


def test_no_match():
    assert kmp_search("abcdef", "gh") == []


def test_pattern_longer_than_text():
    assert kmp_search("short", "longer") == []


def test_empty_pattern_raises():
    with pytest.raises(ValueError):
        kmp_search("text", "")

