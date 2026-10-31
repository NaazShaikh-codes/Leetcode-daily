class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen = set()
        extra = []
        for i in range(len(nums)):
            if nums[i] in seen:
                extra.append(nums[i])
            else:
                seen.add(nums[i])
        return extra
