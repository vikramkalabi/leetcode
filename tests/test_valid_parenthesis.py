import pytest

from leetcode.valid_parenthesis import Solution


def test_longest_common_prefix():
    s = Solution()

    assert s("()")
    assert s("()[]{}")
    assert not s("]")
    assert not s("{}[)(]")
