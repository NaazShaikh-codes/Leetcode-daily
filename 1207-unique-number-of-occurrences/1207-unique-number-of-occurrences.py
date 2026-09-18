class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurence = {}
        for i in arr:
            if i in occurence:
                occurence[i] += 1
            else:
                occurence[i] = 1
        values = list(occurence.values())
        return len(values) == len(set(values))

        