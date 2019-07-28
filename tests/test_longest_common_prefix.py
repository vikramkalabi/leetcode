import pytest

from leetcode.longest_common_prefix import Solution


def test_longest_common_prefix():
    s = Solution()

    assert s(["flower", "flow"]) == "flow"
    assert s(["dog", "racecar", "car"]) == ""
