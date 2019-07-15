import pytest
from leetcode.add_two_numbers import Solution
from leetcode.structures.singly_linked_list import ListNode


def test_add_two_numbers1():

    l1 = ListNode.from_list([3, 4, 2], reversed=True)
    assert str(l1) == "[ 2 4 3 ]"

    l2 = ListNode.from_list([4, 6, 5], reversed=True)
    assert str(l2) == "[ 5 6 4 ]"

    ans = ListNode.from_list([8, 0, 7], reversed=True)
    assert str(ans) == "[ 7 0 8 ]"

    s = Solution()

    assert str(s(l1, l2)) == str(ans)


def test_add_two_numbers2():

    l1 = ListNode.from_list([9, 8])
    assert str(l1) == "[ 9 8 ]"

    l2 = ListNode.from_list([1])
    assert str(l2) == "[ 1 ]"

    ans = ListNode.from_list([0, 9])
    assert str(ans) == "[ 0 9 ]"

    s = Solution()

    assert str(s(l1, l2)) == str(ans)
