class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        pre = 1
        suf = 1
        for i in range(n):
            answer[i] = pre
            pre *= nums[i]
        for i in range(n-1,-1,-1):
            answer[i] *= suf
            suf *= nums[i]

        return answer
        
        
        