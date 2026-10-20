class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = []
        count = 0
        for num in nums:
            digit_sum = sum(int(d) for d in str(num))
            arr.append((digit_sum, num))
        arr.sort()
        sorted_nums = [item[1] for item in arr]
        pos = {num: i for i, num in enumerate(nums)}
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                j = pos[sorted_nums[i]]
                pos[nums[i]] = j
                pos[nums[j]] = i
                nums[i], nums[j] = nums[j], nums[i]
                count += 1
        return count