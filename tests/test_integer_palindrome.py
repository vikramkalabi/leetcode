import pytest
from leetcode.integer_palindrome import Solution


def test_two_sum():
    s = Solution()
    assert s(121)
    assert s(-4121) == False
    assert s(123404321)
