"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""


class Solution:

    # optimized solution (second attempt)
    def lengthOfLongestSubstring(self, s: str) -> int:  # noqa (name)
        """ Runtime: 152 ms | Memory Usage: 14.2 MB """
        # iterate over string
        # hash char into dictionary
        # if char exists
        # record substring (or length)
        # reconstruct valid portion of substring
        #   remove repeated char and all prior chars

        longest_substring = 0
        hashionary = {}
        substring_list = []

        for i, char in enumerate(s):
            # test if char exists
            if hashionary.get(char) is None:
                hashionary[char] = i
                substring_list.append(char)
            else:
                # test for longest substring
                longest_substring = max(longest_substring, len(hashionary))

                # reconstruct valid portion of substring
                # remove duplicate and all previous chars
                split_exclusive = (hashionary[char] + 1 - (i - len(substring_list)))
                removed_chars = substring_list[:split_exclusive]
                substring_list = substring_list[split_exclusive:]
                # hashionary = {k: hashionary[k] for k in substring_list}
                for each in removed_chars:
                    hashionary.pop(each)

                # add current duplicate char
                hashionary[char] = i
                substring_list += char

        longest_substring = max(longest_substring, len(hashionary))

        return longest_substring

    # first solution
    def old_01_lengthOfLongestSubstring(self, s: str) -> int:  # noqa (name)
        """ Runtime: 775 ms | Memory Usage: 14.2 MB """
        # iterate over string
        # hash char into dictionary
        # if char exists
        # record substring (or length)
        # reconstruct valid portion of substring
        #   remove repeated char and all prior chars

        hash_map_current = {}  # sets are immutable in Python
        hash_map_best = {}
        i = 0
        
        while i < len(s):
            # test if char exists
            if hash_map_current.get(s[i]) is None:
                hash_map_current[s[i]] = i
            else:
                # test for greater substring length
                if len(hash_map_current) > len(hash_map_best):
                    hash_map_best = hash_map_current.copy()

                # reconstruct valid portion of substring
                # remove repeated char and all prior chars
                hash_map_current = {k: v for k, v in list(hash_map_current.items()) if v > hash_map_current[s[i]]}
                hash_map_current[s[i]] = i  # add current char (preserves order)

            # increment
            i += 1

        # test for greater substring length
        if len(hash_map_current) > len(hash_map_best):
            hash_map_best = hash_map_current.copy()

        # to return the substring itself:
        #   return ''.join(hash_map_best.keys())

        return (len(hash_map_best.keys()), ''.join(hash_map_best.keys()))[0]

    # sliding window solution (third attempt; less performant)
    def old_03_lengthOfLongestSubstring(self, s: str) -> int:  # noqa (name)
        """ Runtime: 670 ms | Memory Usage: 14 MB """
        start_index = end_index = 0
        longest_substring = 0
        hash_table = {}
        
        while end_index < len(s):
            if hash_table.get(s[end_index]) is None:
                hash_table[s[end_index]] = end_index
                end_index += 1
            else:
                longest_substring = max(longest_substring, len(hash_table))
                start_index = hash_table[s[end_index]] + 1
                end_index = start_index
                hash_table.clear()

        longest_substring = max(longest_substring, len(hash_table))

        return longest_substring


# testing
class Test(Solution):
    test_dict =\
    {
        # provided
        "abcabcbb": 3,
        "pwwkew": 3,
        " ": 1,
        "dvdf": 3,
        # custom
        "nxdavdgfenqo": 9,
        "nxdavdgfenqobz": 11,
        "323nms8SN? 3s emIII3": 10,

    }

    def test_all(self):
        for each_item in self.test_dict.items():
            try:
                assert self.lengthOfLongestSubstring(each_item[0]) == each_item[1]
                print(f"PASS \t {each_item}")
            except AssertionError:
                print(f"FAIL \t {each_item} \t {self.lengthOfLongestSubstring(each_item[0])}")


Test().test_all()
