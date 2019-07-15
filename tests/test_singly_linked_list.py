import pytest


def test_creation_from_list():
    from leetcode.structures.singly_linked_list import ListNode

    node = ListNode.from_list([1, 2, 3], reversed=False)
    assert str(node) == "[ 1 2 3 ]"


def test_creation_from_list_reveresed():
    from leetcode.structures.singly_linked_list import ListNode

    node = ListNode.from_list([1, 2, 3], reversed=True)
    assert str(node) == "[ 3 2 1 ]"
