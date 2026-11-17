class Solution(object):
    def findLucky(self, arr):
        lucky = -1
        for num in set(arr):
            if arr.count(num) == num:
                lucky = max(lucky, num)
        return lucky