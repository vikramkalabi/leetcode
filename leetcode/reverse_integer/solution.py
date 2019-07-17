from leetcode.structures.singly_linked_list import ListNode


class Solution:
    def __call__(self, number):
        sign = -1 if number < 0 else 1
        number = int(str(sign * number)[::-1])
        return sign * number if number <= (2 ** 31) - 1 else 0
