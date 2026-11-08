class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = nums[:n]
        y = nums[n:]
        result = []
        for i in range(n):
            result.append(x[i])
            result.append(y[i])
        return result