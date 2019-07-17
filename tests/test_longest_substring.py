import pytest
from leetcode.longest_substring import Solution


def test_longest_substring1():
    s = Solution()

    assert s("abcabcbb") == 3  # "abc"
    assert s("bbbbb") == 1  # "b"
    assert s("pwwkkew") == 3  # "wke"


def test_longest_substring2():
    s = Solution()

    assert s.solution2("abcabcbb") == 3  # "abc"
    assert s.solution2("bbbbb") == 1  # "b"
    assert s.solution2("pwwkkew") == 3  # "kew"
