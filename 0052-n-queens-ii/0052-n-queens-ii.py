
class Solution:
    def totalNQueens(self, n: int) -> int:
        x = [0] * (n + 1)
        count = 0
        def check(row, col):
            for j in range(1, row):
                if x[j] == col:
                    return False
                if abs(j - row) == abs(x[j] - col):
                    return False
            return True

        def solution(row):
            nonlocal count
            for col in range(1, n + 1):
                if check(row, col):
                    x[row] = col

                    if row == n:
                        count += 1
                    else:
                        solution(row + 1)
        solution(1)
        return count
