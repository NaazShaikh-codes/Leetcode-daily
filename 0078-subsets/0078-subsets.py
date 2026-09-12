class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        from itertools import combinations

        result = []

        for r in range(len(nums) + 1):
            for combination in combinations(nums, r):
                result.append(list(combination))

        return result

        