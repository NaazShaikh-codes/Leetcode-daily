class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        final_set = set(nums)
        max_length = 0
        for num in final_set:
            if num - 1 not in final_set:
                current_num = num
                current_length = 1
                while current_num + 1 in final_set:
                    current_num += 1
                    current_length += 1
                max_length = max(max_length, current_length)
        return max_length
