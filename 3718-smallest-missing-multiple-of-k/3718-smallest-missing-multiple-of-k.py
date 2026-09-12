class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hash_set = set(nums)    
        m = 1
        while k*m in hash_set:
            m+=1
        return m*k