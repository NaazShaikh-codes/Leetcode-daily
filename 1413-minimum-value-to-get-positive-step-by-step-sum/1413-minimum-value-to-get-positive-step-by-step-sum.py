class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            startValue = min(startValue, total)
        return 1 - startValue
            

            
        