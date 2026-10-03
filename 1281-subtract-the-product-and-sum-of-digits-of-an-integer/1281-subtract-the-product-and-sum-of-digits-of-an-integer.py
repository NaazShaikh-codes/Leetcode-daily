class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = str(n)
        total = sum(int(i) for i in digits)
        product = 1
        for i in digits:
            product *= int(i)
        return product - total