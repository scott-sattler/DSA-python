"""
A man, a plan, a canal: Panama
^                            ^

1234
^  ^
1234
 ^^

123
^ ^
123
 ^


edge cases:
    even
    odd
    test pointers for equal or greater than

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ALPHA_NUM = 'abcdefghijklmnopqrstuvwxyz0123456789'
        i = 0
        j = len(s) - 1

        while True:
            if i >= j:
                return True

            left = s[i].lower()
            right = s[j].lower()

            if left not in ALPHA_NUM:
                i += 1
                continue
            if right not in ALPHA_NUM:
                j -= 1
                continue

            if left != right:
                return False

            i += 1
            j -= 1

        return True
