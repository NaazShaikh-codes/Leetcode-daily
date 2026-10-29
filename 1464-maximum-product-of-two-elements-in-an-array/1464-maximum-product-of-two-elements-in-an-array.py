class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_num1 = max(nums)
        nums.remove(max_num1)
        max_num2 = max(nums)
        return (max_num1 - 1) * (max_num2 - 1)