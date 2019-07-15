class Solution:
    def __call__(self, nums, target):
        seen = {}
        for num in nums:
            key = target - num
            if key in seen:
                return [key, num]
            seen[num] = True
        return []
