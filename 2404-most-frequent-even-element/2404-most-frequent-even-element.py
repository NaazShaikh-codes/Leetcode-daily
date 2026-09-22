class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        even_dictionary = {}
        for num in nums:
            if num % 2 == 0:
                if num in even_dictionary:
                    even_dictionary[num] += 1
                else:
                    even_dictionary[num] = 1
        if not even_dictionary:
            return -1

        max_frq = max(even_dictionary.values())
        return min(num for num in even_dictionary if even_dictionary[num] == max_frq)
