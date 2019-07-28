class Solution:
    def __call__(self, words):
        if len(words) <= 1:
            return ""

        common_prefix = ""
        for i, c in enumerate(words[0]):
            for word in words[1:]:
                if i >= len(word) or c != word[i]:
                    return common_prefix
            common_prefix += c
        return common_prefix
