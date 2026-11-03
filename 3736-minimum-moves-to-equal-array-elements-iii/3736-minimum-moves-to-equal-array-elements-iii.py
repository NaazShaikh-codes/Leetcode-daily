class Solution(object):
    def minMoves(self, nums):
        maximum = 0
        count = 0
        for i in nums:
            maximum = max(maximum, i)
        for i in range(len(nums)):
            while nums[i] < maximum:
                nums[i] += 1
                count += 1
        return count