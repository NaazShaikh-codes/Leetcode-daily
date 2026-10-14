
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        array = nums1 + nums2
        array.sort()
        n = len(array)
        if n % 2 == 0:
            mid = n // 2
            return (array[mid] + array[mid - 1]) / 2
        else:
            mid = n // 2
            return array[mid]