class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        #0 -> i and i -> n-1
        for i in range (len(nums)):
            s = max(nums[0:i+1]) - min(nums[i:])
            if s <= k:
                return i
            
        return -1