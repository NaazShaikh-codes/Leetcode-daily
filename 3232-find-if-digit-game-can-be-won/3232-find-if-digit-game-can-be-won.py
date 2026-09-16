class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digits = [x for x in nums if 0 <= x <= 9]
        double_digits = [x for x in nums if x > 9]

        sum1 = sum(single_digits)
        sum2 = sum(double_digits)

        if sum1 != sum2:
            return True

        return False