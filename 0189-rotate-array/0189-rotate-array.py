class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        result = nums[-k:] + nums[:-k]
        nums[:] = result



        

        """
        Do not return anything, modify nums in-place instead.
        """
        