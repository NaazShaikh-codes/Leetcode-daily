class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        sorted_nums = sorted(frequency, key = frequency.get, reverse = True)
        result = sorted_nums[:k]
        return result
            

        