from leetcode.structures.singly_linked_list import ListNode


class Solution:
    def __call__(self, x):
        if x < 0:
            return False

        r = 0
        n = x
        while x > 0:  # before half way x is always > r
            r = r * 10 + (x % 10)
            x //= 10

        return n == r

    def solution2(self, x):
        return str(x) == str(x)[::-1]
