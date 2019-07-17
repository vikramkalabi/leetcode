class Solution:
    def __call__(self, word):
        last_seen = {}
        left_most_valid = 0
        longest = 0
        for i, letter in enumerate(word):
            left_most_valid = max(
                left_most_valid, last_seen.get(letter, -1) + 1
            )
            last_seen[letter] = i
            longest = max(i - left_most_valid + 1, longest)
        return longest

    def solution2(self, word):
        curr_length = max_length = 0
        for i, letter in enumerate(word):
            # see last curr_length characters from i
            index = word[i - curr_length : i].find(letter)
            # change curr_length to (i-curr_length) to length from last seen character index
            curr_length -= index
            max_length = max(max_length, curr_length)
        return max_length
