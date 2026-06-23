from typing import List


class Solution:
    # O(n^2); O(1)
    def twoSum_naive(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if i == j:
                    continue
                if n + m == target:
                    return [i, j]

    # O(n); O(n)
    def twoSum_hmap(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        # generate map of {(target - number): index}
        for i, n in enumerate(nums):
            diff = target - n
            hmap[diff] = i

        for i, n in enumerate(nums):
            if n in hmap and hmap[n] != i:
                return [i, hmap[n]]

if __name__ == '__main__':
    all_solutions = [Solution().twoSum_naive, Solution().twoSum_hmap]
    test_cases: list[tuple[list, int, list]] = [
        (
            [2,7,11,15],
            9,
            [0, 1]
        )
    ]
    for solution in all_solutions:
        print(f'{solution.__name__}:')
        print(f'\tnums, target, actual=?=expected for solution.__name__')
        for tc in test_cases:
            nums, target, expected = tc
            actual = solution(nums, target)
            print(f'\t{nums}, {target}, {actual} =?= {expected} for {solution.__name__} {solution(nums, target) == expected}')
            assert actual == expected