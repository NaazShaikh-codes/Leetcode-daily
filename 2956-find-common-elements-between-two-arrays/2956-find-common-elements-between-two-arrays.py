class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans1 = ans2 = 0
        for num1 in nums1:
            if num1 in nums2:
                ans1 += 1
        for num2 in nums2:
            if num2 in nums1:
                ans2 += 1
        return [ans1,ans2]
        