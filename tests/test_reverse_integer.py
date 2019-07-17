import pytest
from leetcode.reverse_integer import Solution


def test_two_sum():
    s = Solution()
    assert s(321) == 123
    assert s(-4121) == -1214
    assert s(1234056892) == 0
