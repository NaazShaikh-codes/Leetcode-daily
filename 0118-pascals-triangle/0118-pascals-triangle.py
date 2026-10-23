class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascals_triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = pascals_triangle[i-1][j-1] + pascals_triangle[i-1][j]
            pascals_triangle.append(row)
        return pascals_triangle