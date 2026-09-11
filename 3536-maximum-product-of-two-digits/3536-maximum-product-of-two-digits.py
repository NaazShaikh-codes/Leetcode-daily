class Solution:
    def maxProduct(self, n: int) -> int:
        a = str(n)
        a = sorted(a)
        return int(a[-1]) * int(a[-2])
        