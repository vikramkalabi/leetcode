import pytest

from leetcode.merge_two_sorted_lists import Solution


def test_merge_two_sorted_lists():
    from leetcode.structures.singly_linked_list import ListNode

    s = Solution()
    l1 = ListNode.from_list([1, 2, 3], reversed=False)
    l2 = ListNode.from_list([2, 3, 5], reversed=False)
    assert str(s(l1, l2)) == "[ 1 2 2 3 3 5 ]"


def test_creation_from_list_reveresed():
    from leetcode.structures.singly_linked_list import ListNode

    s = Solution()
    l1 = ListNode.from_list([], reversed=False)
    l2 = ListNode.from_list([2, 3, 5], reversed=False)
    assert str(s(l1, l2)) == "[ 2 3 5 ]"
