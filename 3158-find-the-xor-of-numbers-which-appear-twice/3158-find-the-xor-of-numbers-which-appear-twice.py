class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans = 0
        non_repeated = set()
        for i in range(len(nums)):
            if nums[i] not in non_repeated:
                non_repeated.add(nums[i])
            else:
                ans ^= nums[i]
        return ans