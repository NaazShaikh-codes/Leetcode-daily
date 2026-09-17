class Solution:
    def fib(self, n: int) -> int:
        n1, n2 = 0, 1

        for i in range(n):
            n3 = n1 + n2
            n1, n2 = n2, n3

        return n1