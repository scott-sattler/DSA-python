"""
testing for correctness of algorithm
vs
prod testing

all - p/f
all + p/f
about boundary p/f -+
near lower bound
near upper bound

fails beyond constraints

"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        h_set = {}
        for num in nums:
            if num in h_set:
                return True
            h_set[num] = None
        return False


