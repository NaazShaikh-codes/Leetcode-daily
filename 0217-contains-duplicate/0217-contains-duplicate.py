class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        repeated_value = set(nums)
        if len(nums) != len(repeated_value):
            return True
        return False
            