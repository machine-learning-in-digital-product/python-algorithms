import pytest
from src.merge_lists import LinkedList, merge_linked_lists

def build_linked_list(values):
    ll = LinkedList()
    for v in values:
        ll.append(v)
    return ll

@pytest.mark.parametrize("a,b,expected", [
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([], [], []),
    ([1,2,3], [], [1,2,3]),
    ([], [1,2,3], [1,2,3]),
    ([1,1,1], [1,1], [1,1,1,1,1]),
    ([1,3,5], [2,4,6], [1,2,3,4,5,6]),
    ([1,2,7], [3,4,5,6], [1,2,3,4,5,6,7]),
])
def test_merge_linked_lists(a, b, expected):
    l1 = build_linked_list(a)
    l2 = build_linked_list(b)
    merged = merge_linked_lists(l1, l2)
    assert merged.to_list() == expected
    assert l1.to_list() == a
    assert l2.to_list() == b