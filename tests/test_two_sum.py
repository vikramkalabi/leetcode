import pytest
from leetcode.two_sum import Solution


def test_two_sum():
    s = Solution()
    assert s([10, 8, 6, 4, 2], 18) == [10, 8]
    assert s([1, 2, 3], -1) == []
