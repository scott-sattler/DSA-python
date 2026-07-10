class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse_substring(s: str, left: int, right: int) -> None:
            while right > left:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        # reverse entire string
        reverse_substring(s, 0, len(s) - 1)

        # reverse each word
        left = 0
        right = 0
        while right < len(s):
            if s[right] != ' ':
                right += 1
                continue

            next_word = right + 1

            right -= 1
            reverse_substring(s, left, right)

            left = right = next_word

        right -= 1
        reverse_substring(s, left, right)
