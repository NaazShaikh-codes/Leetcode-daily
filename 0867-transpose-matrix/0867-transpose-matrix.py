class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transpose = []
        for col in range(len(matrix[0])):
            new_row = []
            for row in range(len(matrix)):
                new_row.append(matrix[row][col])
            transpose.append(new_row)
        return transpose