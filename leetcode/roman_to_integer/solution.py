class Solution:
    def __call__(self, s):
        char2num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        num = 0
        prev = -1
        for c in s[::-1]:

            curr = char2num[c]
            sign = 1 if curr >= prev else -1
            num += sign * curr
            prev = curr

        return num
