class Solution:
    def climbStairs(self, n: int) -> int:

        n1 = 1
        n2 = 2

        if n == 1:
            return 1

        if n == 2:
            return 2

        for i in range(n - 2):
            new_number = n1 + n2
            n1 = n2
            n2 = new_number

        return n2