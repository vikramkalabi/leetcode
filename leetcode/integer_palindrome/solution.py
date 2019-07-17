from leetcode.structures.singly_linked_list import ListNode


class Solution:
    def __call__(self, x):
        if x < 0:
            return False

        r = 0
        while x > r:  # before half way x is always > r
            r = r * 10 + (x % 10)
            x //= 10

        return x == r

