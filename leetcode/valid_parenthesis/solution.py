class Solution:
    def __call__(self, s):
        matches = {"}": "{", ")": "(", "]": "["}
        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in ")}]":
                if not stack or matches[c] != stack.pop():
                    return False
        return not stack
