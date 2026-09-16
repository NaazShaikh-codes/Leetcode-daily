class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        jump = 0

        for i in range(len(nums)):
            if i <= jump:
                jump = max(jump, i + nums[i])
            else:
                return False

        return True