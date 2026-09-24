class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        unique_list = []
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                unique_list.append(nums[i])
        return sum(unique_list)
        