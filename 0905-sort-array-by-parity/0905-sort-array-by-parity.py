class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        return even + odd
