"""
125. Valid Palindrome
Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 10^5
    s consists only of printable ASCII characters.
"""
import string


class Solution:
    # second; single pass
    # time complexity: O(n)
    # space complexity: O(1)
    def isPalindrome(self, s: str) -> bool:  # noqa: naming convention
        alpha_num = string.printable[:26+10]

        # two pointer, out->in<-out
        l_pointer = 0
        r_pointer = len(s) - 1
        while l_pointer < r_pointer:
            # alpha_num test
            l_char = s[l_pointer].lower()
            if l_char not in alpha_num:
                l_pointer += 1
                continue
            r_char = s[r_pointer].lower()
            if r_char not in alpha_num:
                r_pointer -= 1
                continue

            # equality test
            if l_char != r_char:
                return False
            l_pointer += 1
            r_pointer -= 1

        return True

    # first; correctness
    # time complexity: O(2n) -> O(n)
    # space complexity: O(n)
    def first_attempt_isPalindrome(self, s: str) -> bool:  # noqa: naming convention
        # remove non-alphanumeric
        only_alphanum = ""
        alpha_num = string.printable[:36]  # .printable -> 0-9a-zA-Z<non-alpha>
        for char in s:
            char = char.lower()
            if char in alpha_num:
                only_alphanum += char
        s = only_alphanum

        pointer_l = pointer_r = len(s) // 2
        sub_size = len(s) // 2
        if len(s) % 2 == 0:  # if even
            pointer_l = len(s) // 2 - 1
        else:  # if odd
            sub_size += 1

        # 2 pointer middle out
        i = 0
        while i < sub_size:
            if s[pointer_l - i] != s[pointer_r + i]:
                return False
            i += 1

        return True


# testing
class Test(Solution):
    test_dict =\
    {
        # # provided
        "A man, a plan, a canal: Panama": True,
        "race a car": False,
        " ": True,

        # failed
        "abb": False,
        "aa": True,

        # # alphanumeric test
        string.printable: False,
        string.printable[0:62]: False,

        # additional test cases
        "$&^#(&# #(&#^(& (#^(#&# (#&#^(#&": True,

    }

    def test_all(self) -> None:
        for each_item in self.test_dict.items():
            try:
                assert self.isPalindrome(each_item[0]) == each_item[1]
                print(f"PASS \t {each_item}")
            except AssertionError:
                print(f"FAIL \t {each_item} \t {self.isPalindrome(each_item[0])}")


Test().test_all()
