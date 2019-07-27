import pytest
from leetcode.roman_to_integer import Solution


def test_two_sum():
    s = Solution()
    assert s("II") == 2
    assert s("XIV") == 14
    assert s("CXV") == 115
    assert s("MCMXCIV") == 1994
