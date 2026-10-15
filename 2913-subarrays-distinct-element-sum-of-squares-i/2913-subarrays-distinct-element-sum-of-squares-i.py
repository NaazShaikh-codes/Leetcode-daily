class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub_array = nums[i:j]
                distinct_count = len(set(sub_array))
                total += distinct_count ** 2
        return total