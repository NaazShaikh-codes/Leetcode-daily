class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digit = list(map(int,str(nums[i])))
            if sum(digit) == i:
                return i
        return -1
        