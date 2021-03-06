"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:  # noqa
        # populate reference value
        # iterate over entire list
        #  compare reference to each str
        #  assign reference LCP
        # return longest prefix

        reference = strs.pop(0)
        lcp = reference
        for each_str in strs:
            i = 0
            lcp = ''
            while i < min(len(reference), len(each_str)):
                if reference[i] == each_str[i]:
                    lcp += each_str[i]
                    i += 1
                else:
                    break
            reference = lcp
        return lcp


class Test(Solution):
    tests = [
        (
            ["flower", "flow", "flight"],
            "fl"
        ),
        (
            ["dog","racecar","car"],
            ""
        ),
        (
            ["a"],
            "a"
        ),
        (
            ["b", ""],
            ""
        ),
        (
            ["aaa", "aa", "aaa"],
            "aa"
        ),
        (
            ["baab", "bacb", "b", "cbc"],
            ""
        ),

    ]

    def test_all(self):
        for each_test in self.tests:
            test_input = each_test[0]
            expected_output = each_test[1]
            actual_output = self.longestCommonPrefix(test_input)
            try:
                assert expected_output == actual_output
                print("PASS", end="")
            except AssertionError:
                print("FAIL", end="")
            finally:
                print(f"  \t test_inp: {test_input}\n"
                      f"\t\t expected_out: {expected_output}\n"
                      f"\t\t actual_out: {actual_output}\n")


Test().test_all()
