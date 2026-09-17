class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        nums1.sort()

        smallest_odd = None

        for num in nums1:
            if num % 2 != 0:
                smallest_odd = num
                break

        
        if smallest_odd is None:
            return True

        for num in nums1:
            if num % 2 == 0 and num <= smallest_odd:
                return False

        return True