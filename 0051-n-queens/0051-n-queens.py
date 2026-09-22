class Solution:
    def solveNQueens(self, n):
        x = [0] * (n + 1)
        ans = []
        board = [["."] * n for _ in range(n)]

        def check(row, col):
            for j in range(1, row):
                if x[j] == col:
                    return False
                if abs(j - row) == abs(x[j] - col):
                    return False
            return True

        def solution(row):
            for col in range(1, n + 1):
                if check(row, col):
                    x[row] = col
                    if row == n:
                        for r in range(1, n + 1):
                            board[r - 1][x[r] - 1] = "Q"
                        ans.append(["".join(row) for row in board])
                        for r in range(n):
                            board[r] = ["."] * n
                    else:
                        solution(row + 1)

        solution(1)
        return ans