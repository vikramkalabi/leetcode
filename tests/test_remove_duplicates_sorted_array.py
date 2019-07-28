import pytest

from leetcode.remove_duplocates_sorted_array import Solution


def test_longest_common_prefix():
    s = Solution()

    assert s([1, 2, 2, 3, 3]) == 3
    assert s([1, 1, 2]) == 2
    assert s([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
