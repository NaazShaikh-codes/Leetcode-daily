class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        indices = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                indices.append(i)
        return indices