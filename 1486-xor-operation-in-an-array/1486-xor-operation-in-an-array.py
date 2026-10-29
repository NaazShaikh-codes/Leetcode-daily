class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        i = 0
        while i < n:
            nums.append(start + 2 * i)
            i += 1
        result = 0
        for num in nums:
            result ^= num
        return result