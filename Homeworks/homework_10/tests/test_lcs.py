from src.lcs import longest_common_subsequence


def test_example():
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"


def test_empty_strings():
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("abc", "") == ""
    assert longest_common_subsequence("", "abc") == ""


def test_no_common_characters():
    assert longest_common_subsequence("abc", "def") == ""


def test_full_match():
    assert longest_common_subsequence("python", "python") == "python"


def test_repeated_characters():
    assert longest_common_subsequence("aaaa", "aa") == "aa"

