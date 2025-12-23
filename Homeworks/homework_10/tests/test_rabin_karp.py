import pytest

from src.rabin_karp import rabin_karp_search


def test_single_match():
    assert rabin_karp_search("hello", "ell") == [1]


def test_multiple_overlapping_matches():
    assert rabin_karp_search("banana", "ana") == [1, 3]


def test_no_match():
    assert rabin_karp_search("abcdef", "gh") == []


def test_pattern_longer_than_text():
    assert rabin_karp_search("hi", "high") == []


def test_empty_pattern_raises():
    with pytest.raises(ValueError):
        rabin_karp_search("text", "")

