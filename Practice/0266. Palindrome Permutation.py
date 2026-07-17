class Solution:
    # time: O(2n)
    # space: O(1)
    def canPermutePalindrome(self, s: str) -> bool:
        letter_map = {}
        for letter in s:
            if letter not in letter_map:
                letter_map[letter] = 0
            letter_map[letter] += 1

        seen_odd = 0
        for letter, value in letter_map.items():
            if value % 2 == 0:
                continue

            seen_odd += 1
            if seen_odd > 1:
                return False

        return True
